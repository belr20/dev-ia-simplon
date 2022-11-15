#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Filename:    connect_to_db.py
# @Author:      belr
# @Time:        17/05/2022 23:49
import emoji
import pandas as pd

from pymongo import MongoClient

from data.etl_binance_to_db import uri, DB_NAME, COLLECTION_NAME


def db_connection(mongo_client, database, collection):
    """
    Connect to mongo DB
    :param mongo_client:
    :param database:
    :param collection:
    :return:
    """
    # mongo_client_dbs = mongo_client.list_database_names()
    # print("Available DBs in Mongo server\t", list(mongo_client_dbs))

    db = mongo_client[database]
    print("Selected DATABASE\t\t", db.name)

    # db_collections = db.list_collection_names()
    # print("\nAvailable collections\t\t", list(db_collections))

    col = db[collection]
    print("Selected COLLECTION\t\t", col.name)

    # Create dataframe
    df = pd.DataFrame(list(col.find()))
    # Delete index
    df = df.drop('_id', axis=1)
    # Reorder columns
    df = df[['Date', 'Open', 'High', 'Low', 'Close', 'Volume']]
    # Reformat date
    df['Date'] = pd.to_datetime(df['Date'], infer_datetime_format=True)
    df = df.sort_values('Date')
    return df


if __name__ == '__main__':
    print("CONNECT_TO_DB is running ...")
    try:
        connection = MongoClient(uri)
        print("connection to Mongo server OK :-)")
        dataframe = db_connection(connection, DB_NAME, COLLECTION_NAME)
        print("\nDataframe INFO from", COLLECTION_NAME.name, ":\n")
        print(dataframe.info())
        print("\n" + "=" * 80 + "\n")

        try:
            connection.close()
            print("Mongo server disconnection OK :-)")
        except Exception as e:
            print("Mongo server disconnection FAILED :-( =>", str(e))

    except Exception as e:
        print("connection to Mongo server FAILED =>", str(e))

    print(emoji.emojize("\nEnd of CONNECT_TO_DB :thumbs_up:"))
    print("\n" + "=" * 80 + "\n")
