#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Filename:    manage.py
# @Author:      belr
# @Time:        18/05/2022 22:40
import argparse
# import pandas as pd

from pymongo import MongoClient
from keras.optimizers import Adam
from argparse import ArgumentParser

from crypto_trading_bot.indicators import add_indicators
from data.connect_to_db import db_connexion
from data.etl_binance_to_db import binance_to_db, uri, CRYPTO, DB_NAME, COLLECTION_NAME
# from crypto_trading_bot.rl_bitcoin_trading_bot import CryptoEnv, CryptoAgent, random_games, train_agent, test_agent
from crypto_trading_bot.rl_bitcoin_trading_bot import CryptoEnv, CryptoAgent, random_games, test_agent


# Argument parser configuration
config_parser = ArgumentParser(epilog="Have FUN !", add_help=False)
config_parser.add_argument("-f", "--from-config", help="Specify config file", metavar="FILE")
# args, _ = config_parser.parse_known_args()

formatter = argparse.ArgumentDefaultsHelpFormatter
parser = argparse.ArgumentParser(formatter_class=formatter, parents=[config_parser], description=__doc__)
subparsers = parser.add_subparsers(dest="command", help='Command')

fetch_data = subparsers.add_parser("fetch-data", help='Fetch Bitcoin OHLCV data from Binance marketplace')
random_agent = subparsers.add_parser("random-agent", help='Test random agent with initial balance = 1000 $')
dense_agent = subparsers.add_parser("dense-agent", help='Test dense agent with initial balance = 1000 $')
cnn_agent = subparsers.add_parser("cnn-agent", help='Test CNN agent with initial balance = 1000 $')
lstm_agent = subparsers.add_parser("lstm-agent", help='Test LSTM agent with initial balance = 1000 $')

args = parser.parse_args()


if __name__ == '__main__':
    print('MAIN is runing with', args)
    print("=" * 120)

    try:
        connexion = MongoClient(uri)
        print("Connexion to Mongo server OK @", connexion.HOST, ":", connexion.PORT)
        print("=" * 120)
    except Exception as e:
        print("Connexion to MongoDB server FAILED =>", str(e))

    try:
        if args.command == 'fetch-data':
            binance_to_db(connexion, CRYPTO, path='./data/input/', csv_file=f"{CRYPTO}_Binance_hourly.csv")

        df = db_connexion(connexion, DB_NAME, COLLECTION_NAME)
        print("=" * 120)
        # df = pd.read_csv('./data/input/pricedata.csv')
        df = df.sort_values('Date')
        df = add_indicators(df)  # Insert indicators to df
        print("Dataframe INFO for testing agents")
        print(df.info())

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

            # train_env = CryptoEnv(train_df, lookback_window_size=lookback_window_size)
            # train_agent(train_env, agent, visualize=False, train_episodes=50000, training_batch_size=500)

            test_env = CryptoEnv(
                test_df,
                lookback_window_size=lookback_window_size,
                show_reward=True,
                show_indicators=True
            )
            # test_agent(
            #     test_env,
            #     agent,
            #     visualize=True,
            #     test_episodes=1,
            #     folder="runs/2021_01_18_22_18_Crypto_Trader",
            #     name="1933.71_Crypto_Trader",
            #     comment="",
            # )
            test_agent(
                test_env,
                agent,
                visualize=True,
                test_episodes=1,
                folder="runs/2021_01_21_20_06_Crypto_Trader",
                name="1984.93_Crypto_Trader",
                comment="",
            )
            random_games(test_env, visualize=False, test_episodes=1)

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
            test_env = CryptoEnv(test_df, lookback_window_size=lookback_window_size, show_reward=True,
                                 show_indicators=True)
            test_agent(
                test_env,
                agent,
                visualize=True,
                test_episodes=1,
                folder="runs/2021_01_22_16_34_Crypto_Trader",
                name="2961.57_Crypto_Trader",
                comment="",
            )
            random_games(test_env, visualize=False, test_episodes=1)

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
            test_env = CryptoEnv(
                test_df,
                lookback_window_size=lookback_window_size,
                show_reward=True,
                show_indicators=True
            )
            test_agent(
                test_env,
                agent,
                visualize=True,
                test_episodes=1,
                folder="runs/2021_01_31_20_04_Crypto_Trader",
                name="3146.45_Crypto_Trader",
                comment="",
            )
            random_games(test_env, visualize=False, test_episodes=1)

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
            test_env = CryptoEnv(
                test_df,
                lookback_window_size=lookback_window_size,
                show_reward=True,
                show_indicators=True
            )
            random_games(test_env, visualize=True, test_episodes=1)

    except Exception as e:
        print("Exception occured during agents testing =>" + str(e))

    try:
        connexion.close()
        print("Mongo server disconnexion OK :-)")
    except Exception as e:
        print("Mongo server disconnexion FAILED =>", str(e))
