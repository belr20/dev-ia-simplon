#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Filename:    model.py
# @Author:      belr
# @Time:        18/05/2022 00:57
import os
os.environ['CUDA_VISIBLE_DEVICES'] = '0'
import numpy as np
import tensorflow as tf

from keras import backend as K
from keras.models import Model
from keras.layers import Input, Dense, Flatten, Conv1D, MaxPooling1D, LSTM

# tf.data.experimental.enable_debug_mode()  # For debuging & development
# tf.config.run_functions_eagerly(True)  # For debuging & development
# tf.config.experimental_run_functions_eagerly(True)  # used for debuging and development
tf.compat.v1.disable_eager_execution()  # usually using this for fastest performance
tf.config.experimental.enable_mlir_graph_optimization()

# GPU configuration
gpus = tf.config.experimental.list_physical_devices('GPU')
print("=" * 80)
if len(gpus) > 0:
    print("\nGPU detected, configuring for highest performance\n")
    for device in gpus:
        print("\tName\t\t", device.name)
        print("\tType\t\t", device.device_type)
    try:
        tf.config.experimental.set_memory_growth(gpus[0], True)
    except RuntimeError:
        pass
else:
    print("\nNO GPU device")
print("\n" + "=" * 80 + "\n")


class SharedModel:
    def __init__(self, input_shape, action_space, learning_rate, optimizer, model="Dense"):
        X_input = Input(input_shape)
        self.action_space = action_space

        # Shared CNN layers:
        if model == "CNN":
            X = Conv1D(filters=64, kernel_size=6, padding="same", activation="tanh")(X_input)
            X = MaxPooling1D(pool_size=2)(X)
            X = Conv1D(filters=32, kernel_size=3, padding="same", activation="tanh")(X)
            X = MaxPooling1D(pool_size=2)(X)
            X = Flatten()(X)

        # Shared LSTM layers:
        elif model == "LSTM":
            X = LSTM(512, return_sequences=True)(X_input)
            X = LSTM(256)(X)

        # Shared Dense layers:
        else:
            X = Flatten()(X_input)
            X = Dense(512, activation="relu")(X)

        # Critic model
        V = Dense(512, activation="relu")(X)
        V = Dense(256, activation="relu")(V)
        V = Dense(64, activation="relu")(V)
        value = Dense(1, activation=None)(V)

        self.Critic = Model(inputs=X_input, outputs=value)
        self.Critic.compile(loss=self.critic_ppo2_loss, optimizer=optimizer(learning_rate=learning_rate))

        # Actor model
        A = Dense(512, activation="relu")(X)
        A = Dense(256, activation="relu")(A)
        A = Dense(64, activation="relu")(A)
        output = Dense(self.action_space, activation="softmax")(A)

        self.Actor = Model(inputs=X_input, outputs=output)
        self.Actor.compile(loss=self.ppo_loss, optimizer=optimizer(learning_rate=learning_rate))
        print("=" * 80)
        print(self.Actor.summary())
        print("=" * 80)

    def ppo_loss(self, y_true, y_pred):
        """
        Defined at https://arxiv.org/abs/1707.06347
        :param y_true:
        :param y_pred:
        :return:
        """
        advantages = y_true[:, :1]
        prediction_picks = y_true[:, 1:1 + self.action_space]
        actions = y_true[:, 1 + self.action_space:]

        LOSS_CLIPPING = 0.2
        ENTROPY_LOSS = 0.001

        prob = actions * y_pred
        old_prob = actions * prediction_picks

        prob = K.clip(prob, 1e-10, 1.0)
        old_prob = K.clip(old_prob, 1e-10, 1.0)

        ratio = K.exp(K.log(prob) - K.log(old_prob))

        p1 = ratio * advantages
        p2 = K.clip(ratio, min_value=1 - LOSS_CLIPPING, max_value=1 + LOSS_CLIPPING) * advantages

        actor_loss = -K.mean(K.minimum(p1, p2))

        entropy = -(y_pred * K.log(y_pred + 1e-10))
        entropy = ENTROPY_LOSS * K.mean(entropy)

        total_loss = actor_loss - entropy

        return total_loss

    def actor_predict(self, state):
        return self.Actor.predict(state)

    def critic_ppo2_loss(self, y_true, y_pred):
        value_loss = K.mean((y_true - y_pred) ** 2)  # standard PPO loss
        return value_loss

    def critic_predict(self, state):
        return self.Critic.predict([state, np.zeros((state.shape[0], 1))])


class ActorModel:
    def __init__(self, input_shape, action_space, learning_rate, optimizer):
        X_input = Input(input_shape)
        self.action_space = action_space

        X = Flatten(input_shape=input_shape)(X_input)
        X = Dense(512, activation="relu")(X)
        X = Dense(256, activation="relu")(X)
        X = Dense(64, activation="relu")(X)
        output = Dense(self.action_space, activation="softmax")(X)

        self.Actor = Model(inputs=X_input, outputs=output)
        self.Actor.compile(loss=self.ppo_loss, optimizer=optimizer(learning_rate=learning_rate))
        print("=" * 80)
        print(self.Actor.summary)
        print("=" * 80)

    def ppo_loss(self, y_true, y_pred):
        """
        Defined at https://arxiv.org/abs/1707.06347
        :param y_true:
        :param y_pred:
        :return:
        """
        advantages = y_true[:, :1]
        prediction_picks = y_true[:, 1:1 + self.action_space]
        actions = y_true[:, 1 + self.action_space:]

        LOSS_CLIPPING = 0.2
        ENTROPY_LOSS = 0.001

        prob = actions * y_pred
        old_prob = actions * prediction_picks

        prob = K.clip(prob, 1e-10, 1.0)
        old_prob = K.clip(old_prob, 1e-10, 1.0)

        ratio = K.exp(K.log(prob) - K.log(old_prob))

        p1 = ratio * advantages
        p2 = K.clip(ratio, min_value=1 - LOSS_CLIPPING, max_value=1 + LOSS_CLIPPING) * advantages

        actor_loss = -K.mean(K.minimum(p1, p2))

        entropy = -(y_pred * K.log(y_pred + 1e-10))
        entropy = ENTROPY_LOSS * K.mean(entropy)

        total_loss = actor_loss - entropy

        return total_loss

    def actor_predict(self, state):
        return self.Actor.predict(state)


class CriticModel:
    def __init__(self, input_shape, action_space, learning_rate, optimizer):
        X_input = Input(input_shape)

        V = Flatten(input_shape=input_shape)(X_input)
        V = Dense(512, activation="relu")(V)
        V = Dense(256, activation="relu")(V)
        V = Dense(64, activation="relu")(V)
        value = Dense(1, activation=None)(V)

        self.Critic = Model(inputs=X_input, outputs=value)
        self.Critic.compile(loss=self.critic_ppo2_loss, optimizer=optimizer(learning_rate=learning_rate))

    def critic_ppo2_loss(self, y_true, y_pred):
        value_loss = K.mean((y_true - y_pred) ** 2)  # Standard PPO loss
        return value_loss

    def critic_predict(self, state):
        return self.Critic.predict([state, np.zeros((state.shape[0], 1))])
