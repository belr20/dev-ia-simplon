#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Filename:    rl-bitcoin-trading-bot.py
# @Author:      belr
# @Time:        17/05/2022 21:12
import os
import copy
import random
import numpy as np

from collections import deque
from datetime import datetime

from tensorboardX import SummaryWriter
from keras.optimizers import Adam

from crypto_trading_bot.model import SharedModel
# from crypto_trading_bot.utils import TradingGraph, write_to_file
from crypto_trading_bot.utils import TradingGraph


class CryptoAgent:
    """
    Custom Bitcoin Trading Agent
    """
    def __init__(self, lookback_window_size=50, learning_rate=0.00005,
                 epochs=1, optimizer=Adam, batch_size=32, model=""):
        self.lookback_window_size = lookback_window_size
        self.model = model

        # Action space from 0 to 3, 0 is hold, 1 is buy, 2 is sell
        self.action_space = np.array([0, 1, 2])

        # Folder to save models
        self.log_name = datetime.now().strftime("%Y%m%d_%H%M") + "_Crypto_Trader"

        # State size contains Market (5 items OHLCV) + Orders history (5 items) = 10
        # For the last lookback_window_size steps
        # self.state_size = (self.lookback_window_size, 10)
        self.state_size = (lookback_window_size, 10 + 9)  # +9 indicators for technical analysis

        # Neural Networks part bellow
        self.learning_rate = learning_rate
        self.epochs = epochs
        self.optimizer = optimizer
        self.batch_size = batch_size

        # Create shared Actor-Critic network model
        self.Actor = self.Critic = SharedModel(
            input_shape=self.state_size,
            action_space=self.action_space.shape[0],
            learning_rate=self.learning_rate,
            optimizer=self.optimizer,
            model=self.model,
        )

        # BEFORE without SharedModel

        # Create Actor-Critic network model
        # self.Actor = ActorModel(
        #     input_shape=self.state_size,
        #     action_space=self.action_space.shape[0],
        #     learning_rate=self.learning_rate,
        #     optimizer=self.optimizer,
        # )

        # self.Critic = CriticModel(
        #     input_shape=self.state_size,
        #     action_space=self.action_space.shape[0],
        #     learning_rate=self.learning_rate,
        #     optimizer=self.optimizer,
        # )

    def create_writer(self, initial_balance, normalize_value, train_episodes):
        """
        Create tensorboard writer
        :param initial_balance:
        :param normalize_value:
        :param train_episodes:
        :return:
        """
        self.replay_count = 0
        self.writer = SummaryWriter('runs/' + self.log_name)

        # Create folder to save models
        if not os.path.exists(self.log_name):
            os.makedirs(self.log_name)

        self.start_training_log(initial_balance, normalize_value, train_episodes)

    def start_training_log(self, initial_balance, normalize_value, train_episodes):
        """
        Save training parameters to Parameters.txt file for future
        :param initial_balance:
        :param normalize_value:
        :param train_episodes:
        :return:
        """
        with open(self.log_name + "/Parameters.txt", "w") as params:
            current_date = datetime.now().strftime('%Y%m%d_%H%M')
            params.write(f"training start: {current_date}\n")
            params.write(f"initial_balance: {initial_balance}\n")
            params.write(f"training episodes: {train_episodes}\n")
            params.write(f"lookback_window_size: {self.lookback_window_size}\n")
            params.write(f"lr: {self.learning_rate}\n")
            params.write(f"epochs: {self.epochs}\n")
            params.write(f"batch size: {self.batch_size}\n")
            params.write(f"normalize_value: {normalize_value}\n")
            params.write(f"model: {self.model}\n")

    def end_training_log(self):
        """
        Save training parameters to Parameters.txt file for future
        :return:
        """
        with open(self.log_name + "/Parameters.txt", "a+") as params:
            current_date = datetime.now().strftime('%Y%m%d_%H%M')
            params.write(f"training end: {current_date}\n")

    def get_gaes(self, rewards, dones, values, next_values, gamma=0.99, lamda=0.95, normalize=True):
        deltas = [r + gamma * (1 - d) * nv - v for r, d, nv, v in zip(rewards, dones, next_values, values)]
        deltas = np.stack(deltas)
        gaes = copy.deepcopy(deltas)
        for t in reversed(range(len(deltas) - 1)):
            gaes[t] = gaes[t] + (1 - dones[t]) * gamma * lamda * gaes[t + 1]

        target = gaes + values

        if normalize:
            gaes = (gaes - gaes.mean()) / (gaes.std() + 1e-8)

        return np.vstack(gaes), np.vstack(target)

    def replay(self, states, actions, rewards, predictions, dones, next_states):
        """
        Replay
        :param states:
        :param actions:
        :param rewards:
        :param predictions:
        :param dones:
        :param next_states:
        :return:
        """
        # Reshape memory to appropriate shape for training
        states = np.vstack(states)
        next_states = np.vstack(next_states)
        actions = np.vstack(actions)
        predictions = np.vstack(predictions)

        # Get Critic network predictions
        values = self.Critic.critic_predict(states)
        next_values = self.Critic.critic_predict(next_states)

        # Compute advantages
        advantages, target = self.get_gaes(rewards, dones, np.squeeze(values), np.squeeze(next_values))
        '''
        plt.plot(target,'-')
        plt.plot(advantages,'.')
        ax=plt.gca()
        ax.grid(True)
        plt.show()
        '''
        # Stack everything to numpy array
        y_true = np.hstack([advantages, predictions, actions])

        # Train Actor & Critic networks
        a_loss = self.Actor.Actor.fit(
            states,
            y_true,
            epochs=self.epochs,
            verbose=0,
            shuffle=True,
            batch_size=self.batch_size,
        )
        c_loss = self.Critic.Critic.fit(
            states,
            target,
            epochs=self.epochs,
            verbose=0,
            shuffle=True,
            batch_size=self.batch_size,
        )

        self.writer.add_scalar('Data/actor_loss_per_replay', np.sum(a_loss.history['loss']), self.replay_count)
        self.writer.add_scalar('Data/critic_loss_per_replay', np.sum(c_loss.history['loss']), self.replay_count)
        self.replay_count += 1

        return np.sum(a_loss.history['loss']), np.sum(c_loss.history['loss'])

    def act(self, state):
        """
        Use the network to predict the next action to take, using the model
        :param state:
        :return:
        """
        prediction = self.Actor.actor_predict(np.expand_dims(state, axis=0))[0]
        action = np.random.choice(self.action_space, p=prediction)
        return action, prediction

    def save(self, name="Crypto_Trader", score="", args=[]):
        """
        Save keras model weights
        :param name:
        :param score:
        :param args:
        :return:
        """
        self.Actor.Actor.save_weights(f"{self.log_name}/{score}_{name}_Actor.h5")
        self.Critic.Critic.save_weights(f"{self.log_name}/{score}_{name}_Critic.h5")

        # Log saved model arguments to file
        if len(args) > 0:
            with open(f"{self.log_name}/log.txt", "a+") as log:
                current_time = datetime.now().strftime('%Y%m%d_%H%M%S')
                log.write(f"{current_time}, {args[0]}, {args[1]}, {args[2]}, {args[3]}, {args[4]}\n")

    def load(self, folder, name):
        """
        Load keras model weights
        :param folder:
        :param name:
        :return:
        """
        self.Actor.Actor.load_weights(os.path.join(folder, f"{name}_Actor.h5"))
        self.Critic.Critic.load_weights(os.path.join(folder, f"{name}_Critic.h5"))


class CryptoEnv:
    """
    A custom Bitcoin trading environment
    """
    def __init__(self, dataframe, initial_balance=1000, lookback_window_size=50, render_range=100,
                 show_reward=False, show_indicators=False, normalize_value=40000):
        # Define action space, state size & other custom parameters
        self.df = dataframe.dropna().reset_index()
        self.df_total_steps = len(self.df) - 1
        self.initial_balance = initial_balance
        self.lookback_window_size = lookback_window_size
        self.render_range = render_range  # Range to render in visualization
        self.show_reward = show_reward  # Show order reward in rendered visualization
        self.show_indicators = show_indicators  # Show indicators in rendered visualization

        # Orders history contains the balance, net_worth, crypto_bought, crypto_sold, crypto_held values
        # For the last lookback_window_size steps
        self.orders_history = deque(maxlen=self.lookback_window_size)

        # Market history contains the OHCL values for the last lookback_window_size prices
        self.market_history = deque(maxlen=self.lookback_window_size)

        # Indicators history contains SMAs, BBs, PSAR, MACD & RSI
        self.indicators_history = deque(maxlen=self.lookback_window_size)

        self.normalize_value = normalize_value

    def reset(self, env_steps_size=0):
        """
        Reset the state of the environment to an initial state
        :param env_steps_size:
        :return:
        """
        # Init visualization
        self.visualization = TradingGraph(
            render_range=self.render_range,
            show_reward=self.show_reward,
            show_indicators=self.show_indicators,
        )
        # Limit orders memory for visualization
        self.trades = deque(maxlen=self.render_range)

        self.balance = self.initial_balance
        self.net_worth = self.initial_balance
        self.prev_net_worth = self.initial_balance
        self.crypto_held = 0
        self.crypto_sold = 0
        self.crypto_bought = 0
        self.episode_orders = 0  # Track episode orders count
        self.prev_episode_orders = 0  # Track previous episode orders count
        self.rewards = deque(maxlen=self.render_range)
        self.env_steps_size = env_steps_size
        self.punish_value = 0

        if env_steps_size > 0:  # For TRAIN dataset
            self.start_step = random.randint(self.lookback_window_size, self.df_total_steps - env_steps_size)
            self.end_step = self.start_step + env_steps_size
        else:  # For TEST dataset
            self.start_step = self.lookback_window_size
            self.end_step = self.df_total_steps

        self.current_step = self.start_step

        for i in reversed(range(self.lookback_window_size)):
            current_step = self.current_step - i

            self.orders_history.append(
                [
                    self.balance,
                    self.net_worth,
                    self.crypto_bought,
                    self.crypto_sold,
                    self.crypto_held
                ]
            )

            self.market_history.append(
                [
                    self.df.loc[current_step, 'Open'],
                    self.df.loc[current_step, 'High'],
                    self.df.loc[current_step, 'Low'],
                    self.df.loc[current_step, 'Close'],
                    self.df.loc[current_step, 'Volume']
                ]
            )

            self.indicators_history.append(
                [
                    self.df.loc[current_step, 'sma7'] / self.normalize_value,
                    self.df.loc[current_step, 'sma25'] / self.normalize_value,
                    self.df.loc[current_step, 'sma99'] / self.normalize_value,
                    self.df.loc[current_step, 'bb_bbm'] / self.normalize_value,
                    self.df.loc[current_step, 'bb_bbh'] / self.normalize_value,
                    self.df.loc[current_step, 'bb_bbl'] / self.normalize_value,
                    self.df.loc[current_step, 'psar'] / self.normalize_value,
                    self.df.loc[current_step, 'MACD'] / 400,
                    self.df.loc[current_step, 'RSI'] / 100,
                ]
            )

        state = np.concatenate((self.market_history, self.orders_history), axis=1) / self.normalize_value
        state = np.concatenate((state, self.indicators_history), axis=1)
        return state

    def _next_observation(self):
        """
        Get the data points for the given current_step
        :return:
        """
        self.market_history.append(
            [
                self.df.loc[self.current_step, 'Open'],
                self.df.loc[self.current_step, 'High'],
                self.df.loc[self.current_step, 'Low'],
                self.df.loc[self.current_step, 'Close'],
                self.df.loc[self.current_step, 'Volume']
            ]
        )

        self.indicators_history.append(
            [
                self.df.loc[self.current_step, 'sma7'] / self.normalize_value,
                self.df.loc[self.current_step, 'sma25'] / self.normalize_value,
                self.df.loc[self.current_step, 'sma99'] / self.normalize_value,
                self.df.loc[self.current_step, 'bb_bbm'] / self.normalize_value,
                self.df.loc[self.current_step, 'bb_bbh'] / self.normalize_value,
                self.df.loc[self.current_step, 'bb_bbl'] / self.normalize_value,
                self.df.loc[self.current_step, 'psar'] / self.normalize_value,
                self.df.loc[self.current_step, 'MACD'] / 400,
                self.df.loc[self.current_step, 'RSI'] / 100,
            ]
        )

        obs = np.concatenate((self.market_history, self.orders_history), axis=1) / self.normalize_value
        obs = np.concatenate((obs, self.indicators_history), axis=1)
        return obs

    def step(self, action):
        """
        Execute one time step within the environment
        :param action:
        :return:
        """
        self.crypto_bought = 0
        self.crypto_sold = 0
        self.current_step += 1

        # Set the current price to a random price between Open & Close
        # current_price = random.uniform(
        #     self.df.loc[self.current_step, 'Open'],
        #     self.df.loc[self.current_step, 'Close']
        # )
        current_price = self.df.loc[self.current_step, 'Open']
        date = self.df.loc[self.current_step, 'Date']  # for visualization
        high = self.df.loc[self.current_step, 'High']  # for visualization
        low = self.df.loc[self.current_step, 'Low']  # for visualization

        if action == 0:  # Hold
            pass

        elif action == 1 and self.balance > self.initial_balance / 100:
            # Buy with 100% of current balance
            self.crypto_bought = self.balance / current_price
            self.balance -= self.crypto_bought * current_price
            self.crypto_held += self.crypto_bought
            self.trades.append(
                {
                    'Date': date,
                    'High': high,
                    'Low': low,
                    'total': self.crypto_bought,
                    'type': "buy",
                    'current_price': current_price,
                }
            )
            self.episode_orders += 1

        elif action == 2 and self.crypto_held > 0:
            # Sell 100% of current crypto held
            self.crypto_sold = self.crypto_held
            self.balance += self.crypto_sold * current_price
            self.crypto_held -= self.crypto_sold
            self.trades.append(
                {
                    'Date': date,
                    'High': high,
                    'Low': low,
                    'total': self.crypto_sold,
                    'type': "sell",
                    'current_price': current_price,
                }
            )
            self.episode_orders += 1

        self.prev_net_worth = self.net_worth
        self.net_worth = self.balance + self.crypto_held * current_price

        self.orders_history.append(
            [
                self.balance,
                self.net_worth,
                self.crypto_bought,
                self.crypto_sold,
                self.crypto_held
            ]
        )

        # For debuging purpose
        # write_to_file(date, self.orders_history[-1])

        # Calculate reward
        # reward = self.net_worth - self.prev_net_worth

        # Receive calculated reward
        reward = self.get_reward()

        if self.net_worth <= self.initial_balance / 2:
            done = True
        else:
            done = False

        obs = self._next_observation() / self.normalize_value

        return obs, reward, done

    def get_reward(self):
        """
        Calculate reward
        :return:
        """
        self.punish_value += self.net_worth * 0.00001
        if self.episode_orders > 1 and self.episode_orders > self.prev_episode_orders:
            self.prev_episode_orders = self.episode_orders
            if self.trades[-1]['type'] == "buy" and self.trades[-2]['type'] == "sell":
                reward = self.trades[-2]['total'] * self.trades[-2]['current_price'] - \
                         self.trades[-2]['total'] * self.trades[-1]['current_price']
                reward -= self.punish_value
                self.punish_value = 0
                self.trades[-1]["Reward"] = reward
                return reward
            elif self.trades[-1]['type'] == "sell" and self.trades[-2]['type'] == "buy":
                reward = self.trades[-1]['total'] * self.trades[-1]['current_price'] - \
                         self.trades[-2]['total'] * self.trades[-2]['current_price']
                reward -= self.punish_value
                self.punish_value = 0
                self.trades[-1]["Reward"] = reward
                return reward
        else:
            return 0 - self.punish_value

    def render(self, visualize=False):
        """
        Render environment
        :param visualize:
        :return:
        """
        if visualize:
            img = self.visualization.render(self.df.loc[self.current_step], self.net_worth, self.trades)
            return img
        # else:
        #     print(f'Step {self.current_step}\tNET WORTH = {round(self.net_worth, 2)}')


def random_games(env, visualize, test_episodes=50, comment=""):
    """
    Play RANDOM Agent
    :param env:
    :param visualize:
    :param test_episodes:
    :param comment:
    :return:
    """
    average_net_worth = 0
    average_orders = 0
    no_profit_episodes = 0

    for episode in range(test_episodes):
        state = env.reset()
        while True:
            env.render(visualize)
            action = np.random.randint(3, size=1)[0]
            state, reward, done = env.step(action)

            if env.current_step == env.end_step:
                average_net_worth += env.net_worth
                average_orders += env.episode_orders
                if env.net_worth < env.initial_balance:
                    # Calculate episode count where negative profit through episode
                    no_profit_episodes += 1
                print("=" * 120)
                print("Episode {}".format(episode))
                print("\tOrders\t\t\t{}".format(env.episode_orders))
                print("\tNET WORTH\t\t{:.2f}".format(env.net_worth))
                print("\tAverage NET WORTH\t{:.2f}".format(average_net_worth / (episode + 1)))
                print("=" * 120)
                break

    print("\nRANDOM Agent AVERAGE for {} episodes\n\tNET WORTH = {:.2f}\tOrders = {}\n".format(
        test_episodes,
        average_net_worth / test_episodes,
        average_orders / test_episodes,
    ))

    # Save test results to test_results.txt file
    with open("logs/test_results.txt", "a+") as results:
        current_date = datetime.now().strftime('%Y-%m-%d %H:%M')
        results.write(f'{current_date}, {"Random games"}, test episodes:{test_episodes}')
        results.write(f', net worth:{average_net_worth / (test_episodes + 1)}, \
        orders per episode:{average_orders / test_episodes}')
        results.write(f', no profit episodes:{no_profit_episodes}, comment: {comment}\n')


def train_agent(env, agent, visualize=False, train_episodes=50, training_batch_size=500):
    """
    Train RL Agent
    :param env:
    :param agent:
    :param visualize:
    :param train_episodes:
    :param training_batch_size:
    :return:
    """
    # Create TensorBoard writer
    agent.create_writer(env.initial_balance, env.normalize_value, train_episodes)
    # Save recent 100 episodes net worth
    total_average = deque(maxlen=100)
    # Used to track BEST average net worth
    best_average = 0

    for episode in range(train_episodes):
        state = env.reset(env_steps_size=training_batch_size)
        states, actions, rewards, predictions, dones, next_states = [], [], [], [], [], []

        for t in range(training_batch_size):
            env.render(visualize)
            action, prediction = agent.act(state)
            next_state, reward, done = env.step(action)
            states.append(np.expand_dims(state, axis=0))
            next_states.append(np.expand_dims(next_state, axis=0))
            action_onehot = np.zeros(3)
            action_onehot[action] = 1
            actions.append(action_onehot)
            rewards.append(reward)
            dones.append(done)
            predictions.append(prediction)
            state = next_state

        a_loss, c_loss = agent.replay(states, actions, rewards, predictions, dones, next_states)
        total_average.append(env.net_worth)
        average = np.average(total_average)

        agent.writer.add_scalar('Data/average net_worth', average, episode)
        agent.writer.add_scalar('Data/episode_orders', env.episode_orders, episode)

        print("=" * 120)
        print("Episode", episode)
        print("\tOrders = {}".format(env.episode_orders))
        print("\tAverage = {:.2f}".format(average))
        print("\tNET WORTH = {:.2f}".format(env.net_worth))
        print("=" * 120)

        if episode > len(total_average):

            if best_average < average:
                best_average = average
                print("BEST average => saving model")
                agent.save(
                    score="{:.2f}".format(best_average),
                    args=[episode, average, env.episode_orders, a_loss, c_loss],
                )

            agent.save()

    agent.end_training_log()


def test_agent(env, agent, visualize=True, test_episodes=10, folder="", name="Crypto_Trader", comment=""):
    """
    Test RL Agent
    :param env:
    :param agent:
    :param visualize:
    :param test_episodes:
    :param folder:
    :param name:
    :param comment:
    :return:
    """
    agent.load(folder, name)
    average_net_worth = 0
    average_orders = 0
    no_profit_episodes = 0

    for episode in range(test_episodes):
        state = env.reset()
        while True:
            env.render(visualize)
            action, prediction = agent.act(state)
            state, reward, done = env.step(action)

            if env.current_step == env.end_step:
                average_net_worth += env.net_worth
                average_orders += env.episode_orders

                if env.net_worth < env.initial_balance:
                    # Calculate episode count where negative profit through episode
                    no_profit_episodes += 1

                print("=" * 120)
                print("Episode", episode)
                print("\tOrders\t\t\t{}".format(env.episode_orders))
                print("\tNET WORTH\t\t{:.2f}".format(env.net_worth))
                print("\tAverage NET WORTH\t{:.2f}".format(average_net_worth / (episode + 1)))
                print("=" * 120)
                break

    print("\nRL Agent results for {} TEST episodes :\n".format(test_episodes))
    print("\tNET WORTH\t\t{:.2f}".format(average_net_worth / test_episodes))
    print("\tOrders\t\t\t{:.0f}".format(average_orders / test_episodes))
    print("\tNO PROFIT episodes\t{}".format(no_profit_episodes))

    # Save test results to test_results.txt file
    with open("logs/test_results.txt", "a+") as results:
        current_date = datetime.now().strftime('%Y-%m-%d %H:%M')
        results.write(f'{current_date}, {name}, test episodes:{test_episodes}')
        results.write(f', net worth:{average_net_worth / (test_episodes + 1)}, \
        orders per episode:{average_orders / test_episodes}')
        results.write(f', no profit episodes:{no_profit_episodes}, model: {agent.model}, comment: {comment}\n')
