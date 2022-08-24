#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Filename:    etl_binance_to_db.py
# @Author:      belr
# @Time:        18/05/2022 23:09
import os
import ssl
import emoji
import asyncio
import datetime
import pandas as pd

from tqdm import tqdm
from sys import platform
from decouple import config
from pymongo import MongoClient


# Globales
CRYPTO = 'BTCUSDT'
DATE_FORMAT = "%Y-%m-%d %H:%M:%S"

# To avoid this ERROR => Scraping: SSL: CERTIFICATE_VERIFY_FAILED
ssl._create_default_https_context = ssl._create_unverified_context

# MongoDB configuration
# DB_USER = '<your_mongo_user_name_here'
DB_USER = config('DB_USER')
# DB_PASSWD = '<your_mongo_user_password_here'
DB_PASSWD = config('DB_PASSWD')

# DB_HOST = 'localhost'
DB_HOST = config('DB_HOST', default='localhost')
# DB_PORT=27017
DB_PORT = config('DB_PORT', default='27017')
# DB_NAME = 'hourlyCryptosOhlcvDB'
DB_NAME = config('DB_NAME', default='hourlyCryptosOhlcvDB')
# COLLECTION_NAME = 'BTCUSDT_BinanceHourly'
COLLECTION_NAME = config('COLLECTION_NAME', default='BTCUSDT_BinanceHourly')

if platform == "win32":
    # Windows
    # uri = "mongodb://%s:%s" % (DB_HOST, DB_PORT)
    uri = "mongodb://%s:%s@%s" % (DB_USER, DB_PASSWD, DB_HOST)
else:
    # Linux
    uri = "mongodb://%s:%s@%s" % (DB_USER, DB_PASSWD, DB_HOST)

# print("\nMongo URI => ", uri)


def doc_in_collection_update(mongo_client, database, collection, dict_list, date_format):
    """
    Update Mongo collection from a dictionnary list WITHOUT duplicates
    :param mongo_client:
    :param database:
    :param collection:
    :param dict_list:
    :param date_format:
    :return:
    """
    try:
        db = mongo_client[database]
        print("Selected DATABASE\t\t", db.name)
        col = db[collection]
        print("Selected COLLECTION\t\t", col.name)
        inserted_docs = []
        for doc in tqdm(dict_list, ascii=True, desc="Update in progress"):
            result = col.update_one(
                {
                    "Date": {
                        '$eq': datetime.datetime.strptime(doc["Date"], date_format)
                    }
                },
                {
                    "$set": {
                        "Open": doc["Open"],
                        "High": doc["High"],
                        "Low": doc["Low"],
                        "Close": doc["Close"],
                        "Volume": doc["Volume"],
                    }
                },
                upsert=True)

            if result.matched_count == 0:
                inserted_docs.append(result.upserted_id)

        print("Update in MongoDB RESULTS =>\t", len(inserted_docs), "documents INSERTED")

    except Exception as e:
        print("Update FAILED in MongoDB =>", str(e))

    print("\n" + "=" * 120 + "\n")


async def save_url_to_csv(crypto, path, file_name):
    """
    Save OHLCV data from marketplace URL to CSV file
    :param crypto:
    :param path:
    :param file_name:
    :return:
    """
    url = f"https://www.cryptodatadownload.com/cdd/Binance_{crypto}_1h.csv"
    print("Download from URL\t\t", url)
    print("\n" + "=" * 120 + "\n")
    df = pd.read_csv(url, header=1)
    final_path = os.path.join(path, file_name)
    csv_file = df.to_csv(final_path, index=False)
    return csv_file


async def save_csv_to_db(mongo_client, path, csv_file, date_format, collection_name):
    """
    Save OHLCV data from CSV to MongoDB
    :param mongo_client:
    :param path:
    :param csv_file:
    :param date_format:
    :param collection_name:
    :return:
    """
    # client_dbs = mongo_client.list_database_names()
    # print("Available DBs in MongoDB server\t", client_dbs)

    # Data preprocessing
    dataframe = pd.read_csv(f"{path}{csv_file}")
    dataframe = dataframe.dropna(thresh=2)
    dataframe = dataframe.drop(['unix', 'symbol', 'Volume USDT', 'tradecount'], axis=1)
    dataframe.columns = ['Date', 'Open', 'High', 'Low', 'Close', 'Volume']
    dataframe['Date'] = pd.to_datetime(dataframe['Date'], format=date_format, errors='coerce')
    dataframe['Date'] = dataframe['Date'].dt.strftime(date_format)
    dataframe = dataframe.dropna(how='any', axis=0)
    dataframe = dataframe.sort_values('Date')

    data_dict = dataframe.to_dict('records')
    doc_in_collection_update(mongo_client, DB_NAME, collection_name, data_dict, date_format)


async def save_url_to_db(mongo_client, crypto, path, csv_file):
    """
    Save OHLCV data from marketplace URL to MongoDB
    :param mongo_client:
    :param crypto:
    :param path:
    :param csv_file:
    :return:
    """
    task_url_to_csv = asyncio.create_task(save_url_to_csv(crypto, path, csv_file))
    task_csv_to_db = asyncio.create_task(save_csv_to_db(mongo_client, path, csv_file, DATE_FORMAT, COLLECTION_NAME))
    tasks = [task_url_to_csv, task_csv_to_db]
    await asyncio.wait(tasks)


def binance_to_db(mongo_client, crypto, path, csv_file):
    """
    Save OHLCV data for crypto from Binance marketplace to MongoDB
    :param mongo_client:
    :param crypto:
    :param path:
    :param csv_file:
    :return:
    """
    loop = asyncio.get_event_loop()
    loop.run_until_complete(save_url_to_db(mongo_client, crypto, path, csv_file))
    loop.close()


if __name__ == '__main__':
    print('\nETL Binance script is running ...\n')

    try:
        connection = MongoClient(uri)
        print("connection to Mongo server\t@",
              connection.HOST, ":", connection.PORT)

        print("\n" + "=" * 120 + "\n")

        binance_to_db(connection, CRYPTO, path="./input/", csv_file=f"{CRYPTO}_Binance_hourly.csv")

        try:
            connection.close()
            print("MongoDB server disconnection OK :-)")
        except Exception as e:
            print("MongoDB server disconnection FAILED =>", str(e))

    except Exception as e:
        print("connection to MongoDb server FAILED =>", str(e))

    print(emoji.emojize("\nEnd of ETL Binance script :thumbs_up:"))
    print("\n" + "=" * 120 + "\n")
