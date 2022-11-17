#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Filename:    main.py
# @Author:      belr
# @Time:        18/05/2022 22:40
import argparse
from argparse import ArgumentParser
# Argument parser configuration
config_parser = ArgumentParser(epilog="Have FUN !", add_help=False)
config_parser.add_argument(
    "--visualize",
    action="store_true",
    help='Render data in OHLCV graph'
)
config_parser.add_argument(
    "--show-indicators",
    action="store_true",
    help='Render technical indicators for analysis'
)
config_parser.add_argument(
    "--show-reward",
    action="store_true",
    help='Render RL agent rewards'
)
config_parser.add_argument(
    "--train",
    action="store_true",
    help='Train RL agent'
)
formatter = argparse.ArgumentDefaultsHelpFormatter
parser = argparse.ArgumentParser(
    formatter_class=formatter,
    parents=[config_parser],
    description=__doc__
)
subparsers = parser.add_subparsers(
    dest="command",
    help='Command'
)

fetch_data = subparsers.add_parser(
    "fetch-data",
    help='Fetch Bitcoin OHLCV data from Binance marketplace'
)
random_agent = subparsers.add_parser(
    "random-agent",
    help='Test random agent with initial balance = 1000 $'
)
dense_agent = subparsers.add_parser(
    "dense-agent",
    help='Test dense agent with initial balance = 1000 $'
)
cnn_agent = subparsers.add_parser(
    "cnn-agent",
    help='Test CNN agent with initial balance = 1000 $'
)
lstm_agent = subparsers.add_parser(
    "lstm-agent",
    help='Test LSTM agent with initial balance = 1000 $'
)
args = parser.parse_args()

# https://stackoverflow.com/a/47227886/15513730
# Uncomment to hide tensorflow compilation warnings
# import os
# os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

from data.etl_binance_to_db import (COLLECTION_NAME, CRYPTO, DB_NAME,
                                    binance_to_db, uri)
from data.connect_to_db import db_connection
from crypto_trading_bot.rl_bitcoin_trading_bot import (CryptoAgent, CryptoEnv,
                                                       random_games,
                                                       test_agent, train_agent)
from crypto_trading_bot.indicators import add_indicators
# from tensorflow.keras.optimizers import Adam
from keras.optimizers import Adam
from pymongo import MongoClient

# import pandas as pd
import emoji
import time


if __name__ == '__main__':
    start_time = time.time()
    print('MAIN is running through following namespace :\n')
    for key, value in vars(args).items():
        print(f'\t{str.upper(key)}\n\t\t\t\t{value}')

    print("\n" + "=" * 80 + "\n")

    try:
        connection = MongoClient(uri)
        print(
            f"Connection to Mongo server\t@{connection.HOST}:{connection.PORT}"
        )

        try:
            if args.command == 'fetch-data':
                binance_to_db(
                    connection,
                    CRYPTO,
                    path='./data/input/',
                    csv_file=f"{CRYPTO}_Binance_hourly.csv"
                )
            else:
                # df = pd.read_csv('./data/input/pricedata.csv')
                # df = df.sort_values('Date')
                df = db_connection(connection, DB_NAME, COLLECTION_NAME)
                df = add_indicators(df)  # Insert indicators to df
                print("Dataframe INFO :\n")
                print(df.info())
                print("\n" + "=" * 80 + "\n")

                lookback_window_size = 50
                test_window = 720  # Last 30 days for TEST dataset
                train_df = df[:-test_window - lookback_window_size]
                test_df = df[-test_window - lookback_window_size:]

                if args.command == 'dense-agent':
                    # Dense network
                    agent = CryptoAgent(
                        lookback_window_size=lookback_window_size,
                        learning_rate=0.00001,
                        epochs=1,
                        optimizer=Adam,
                        batch_size=32,
                        model="Dense",
                    )

                    if args.train:
                        train_env = CryptoEnv(
                            train_df,
                            lookback_window_size=lookback_window_size
                        )
                        train_agent(
                            train_env,
                            agent,
                            visualize=False,
                            train_episodes=50000,
                            training_batch_size=500
                        )
                    else:
                        test_env = CryptoEnv(
                            test_df,
                            lookback_window_size=lookback_window_size,
                            show_reward=args.show_reward,
                            show_indicators=args.show_indicators,
                        )
                        test_agent(
                            test_env,
                            agent,
                            visualize=args.visualize,
                            test_episodes=1,
                            folder="runs/2021_01_21_20_06_Crypto_Trader",
                            name="1984.93_Crypto_Trader",
                            comment="",
                        )
                        random_games(
                            test_env,
                            visualize=False,
                            test_episodes=1
                        )

                if args.command == 'cnn-agent':
                    # CNN network
                    agent = CryptoAgent(
                        lookback_window_size=lookback_window_size,
                        learning_rate=0.00001,
                        epochs=1,
                        optimizer=Adam,
                        batch_size=32,
                        model="CNN",
                    )
                    if args.train:
                        train_env = CryptoEnv(
                            train_df,
                            lookback_window_size=lookback_window_size
                        )
                        train_agent(
                            train_env,
                            agent,
                            visualize=False,
                            train_episodes=50000,
                            training_batch_size=500
                        )
                    else:
                        test_env = CryptoEnv(
                            test_df,
                            lookback_window_size=lookback_window_size,
                            show_reward=args.show_reward,
                            show_indicators=args.show_indicators,
                        )
                        test_agent(
                            test_env,
                            agent,
                            visualize=args.visualize,
                            test_episodes=1,
                            folder="runs/2021_01_22_16_34_Crypto_Trader",
                            name="2961.57_Crypto_Trader",
                            comment="",
                        )
                        random_games(
                            test_env,
                            visualize=False,
                            test_episodes=1
                        )

                if args.command == 'lstm-agent':
                    # LSTM network
                    agent = CryptoAgent(
                        lookback_window_size=lookback_window_size,
                        learning_rate=0.00001,
                        epochs=1,
                        optimizer=Adam,
                        batch_size=128,
                        model="LSTM",
                    )
                    if args.train:
                        train_env = CryptoEnv(
                            train_df,
                            lookback_window_size=lookback_window_size
                        )
                        train_agent(
                            train_env,
                            agent,
                            visualize=False,
                            train_episodes=50000,
                            training_batch_size=500
                        )
                    else:
                        test_env = CryptoEnv(
                            test_df,
                            lookback_window_size=lookback_window_size,
                            show_reward=args.show_reward,
                            show_indicators=args.show_indicators,
                        )
                        test_agent(
                            test_env,
                            agent,
                            visualize=args.visualize,
                            test_episodes=1,
                            folder="runs/2021_01_31_20_04_Crypto_Trader",
                            name="3146.45_Crypto_Trader",
                            comment="",
                        )
                        random_games(
                            test_env,
                            visualize=False,
                            test_episodes=1
                        )

                if args.command == 'random-agent':
                    # LSTM network
                    agent = CryptoAgent(
                        lookback_window_size=lookback_window_size,
                        learning_rate=0.00001,
                        epochs=1,
                        optimizer=Adam,
                        batch_size=128,
                        model="LSTM",
                    )
                    if args.train:
                        train_env = CryptoEnv(
                            train_df,
                            lookback_window_size=lookback_window_size
                        )
                        train_agent(
                            train_env,
                            agent,
                            visualize=False,
                            train_episodes=50000,
                            training_batch_size=500
                        )
                    else:
                        test_env = CryptoEnv(
                            test_df,
                            lookback_window_size=lookback_window_size,
                            show_reward=args.show_reward,
                            show_indicators=args.show_indicators,
                        )
                        random_games(
                            test_env,
                            visualize=args.visualize,
                            test_episodes=1
                        )

        except Exception as e:
            print("Exception occured in MAIN =>", str(e))
            print("\n" + "=" * 80 + "\n")

        try:
            connection.close()
        except Exception as e:
            print("Mongo server disconnection FAILED =>", str(e))
            print("\n" + "=" * 80 + "\n")

    except Exception as e:
        print("Connection to Mongo server FAILED =>", str(e))
        print("\n" + "=" * 80 + "\n")

    elapsed_time = time.time() - start_time
    execution_time = time.strftime("%M:%S", time.gmtime(elapsed_time))
    print(emoji.emojize(f"End of MAIN after {execution_time} :thumbs_up:"))
    print("\n" + "=" * 80 + "\n")
