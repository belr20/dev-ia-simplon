#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Filename:    indicators.py
# @Author:      belr
# @Time:        18/05/2022 18:38
import pandas as pd

from crypto_trading_bot.utils import plot_ohlc

from ta.momentum import rsi
from ta.volatility import BollingerBands
from ta.trend import SMAIndicator, macd, PSARIndicator


def add_indicators(dataframe):
    """
    Add indicators
    :type
    :param dataframe:
    :return:
    """
    # Add Simple Moving Average (SMA) indicators
    dataframe["sma7"] = SMAIndicator(close=dataframe["Close"], window=7, fillna=True).sma_indicator()
    dataframe["sma25"] = SMAIndicator(close=dataframe["Close"], window=25, fillna=True).sma_indicator()
    dataframe["sma99"] = SMAIndicator(close=dataframe["Close"], window=99, fillna=True).sma_indicator()

    # Add Bollinger Bands indicator
    indicator_bb = BollingerBands(close=dataframe["Close"], window=20, window_dev=2)
    dataframe['bb_bbm'] = indicator_bb.bollinger_mavg()
    dataframe['bb_bbh'] = indicator_bb.bollinger_hband()
    dataframe['bb_bbl'] = indicator_bb.bollinger_lband()

    # Add Parabolic Stop and Reverse (Parabolic SAR) indicator
    indicator_psar = PSARIndicator(
        high=dataframe["High"],
        low=dataframe["Low"],
        close=dataframe["Close"],
        step=0.02,
        max_step=2,
        fillna=True,
    )
    dataframe['psar'] = indicator_psar.psar()

    # Add Moving Average Convergence Divergence (MACD) indicator
    dataframe["MACD"] = macd(close=dataframe["Close"], window_slow=26, window_fast=12, fillna=True)  # mazas

    # Add Relative Strength Index (RSI) indicator
    dataframe["RSI"] = rsi(close=dataframe["Close"], window=14, fillna=True)  # mazas

    return dataframe


if __name__ == "__main__":
    df = pd.read_csv('../data/input/pricedata.csv')
    df = df.sort_values('Date')
    df = add_indicators(df)

    test_df = df[-400:]

    plot_ohlc(df)
