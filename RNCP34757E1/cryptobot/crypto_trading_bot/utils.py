#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Filename:    utils.py
# @Author:      belr
# @Time:        17/05/2022 21:10
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mpl_dates

from collections import deque
from datetime import datetime
# from matplotlib.colors import rgb2hex
from mplfinance.original_flavor import candlestick_ohlc

import cv2


logger = []


def write_to_file(date, order, filename='{}.txt'.format(datetime.now().strftime("%Y%m%d-%H%M%S_trading-report"))):
    """
    For debuging purpose ('Date', 'balance', 'net_worth', 'buy', 'sell', 'hold')
    :param date:
    :param order:
    :param filename:
    :return:
    """
    for item in order:
        date += " {}".format(item)
    # print(date)
    if not os.path.exists('logs'):
        os.makedirs('logs')
    file = open("logs/" + filename, 'a+')
    file.write(date + "\n")
    file.close()


# def rgb_to_lab(img):
#     img_rgb = rgb2hex(img)
#     Lab = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2LAB)
#     return Lab


class TradingGraph:
    """
    A crypto trading visualization using matplotlib made to render custom prices which come in following way:
    date, open, high, low, close, volume, net_worth, trades
    Call render every step
    """
    def __init__(self, render_range, show_reward=False, show_indicators=False):
        self.volume = deque(maxlen=render_range)
        self.net_worth = deque(maxlen=render_range)
        self.render_data = deque(maxlen=render_range)
        self.render_range = render_range
        self.show_reward = show_reward
        self.show_indicators = show_indicators
        # Other parameters
        self.RSI = None
        self.MACD = None
        self.psar = None
        self.bb_bbl = None
        self.bb_bbh = None
        self.bb_bbm = None
        self.sma99 = None
        self.sma25 = None
        self.sma7 = None
        self.ax4 = None

        # We are using the style ‘ggplot’
        plt.style.use('ggplot')
        # close all plots if there are open
        plt.close('all')

        # figsize attribute allows us to specify the width and height of a figure in unit inches
        self.fig = plt.figure(figsize=(16, 8), num="Bitcoin Trading Bot")

        # Create top subplot for price axis
        self.ax1 = plt.subplot2grid((6, 1), (0, 0), rowspan=5, colspan=1)

        # Create bottom subplot for volume which shares its x-axis
        self.ax2 = plt.subplot2grid((6, 1), (5, 0), rowspan=1, colspan=1, sharex=self.ax1)

        # Create a new axis for net worth which shares its x-axis with price
        self.ax3 = self.ax1.twinx()

        # Formatting date
        self.date_format = mpl_dates.DateFormatter('%d-%m-%Y')

        # Add paddings to make graph easier to view
        # plt.subplots_adjust(left=0.07, bottom=-0.1, right=0.93, top=0.97, wspace=0, hspace=0)
        # Replaced by `tight_layout() in render function`

        # define if show indicators
        if self.show_indicators:
            self.create_indicators_lists()

    def create_indicators_lists(self):
        """
        Create indicators to render for technical analysis
        :return: 
        """
        # Create a new axis for indicatorswhich shares its x-axis with volume
        self.ax4 = self.ax2.twinx()

        self.sma7 = deque(maxlen=self.render_range)
        self.sma25 = deque(maxlen=self.render_range)
        self.sma99 = deque(maxlen=self.render_range)

        self.bb_bbm = deque(maxlen=self.render_range)
        self.bb_bbh = deque(maxlen=self.render_range)
        self.bb_bbl = deque(maxlen=self.render_range)

        self.psar = deque(maxlen=self.render_range)

        self.MACD = deque(maxlen=self.render_range)
        self.RSI = deque(maxlen=self.render_range)

    def plot_indicators(self, df, date_render_range):
        """
        Plot indicators for technical analysis
        :param df:
        :param date_render_range:
        :return:
        """
        self.sma7.append(df["sma7"])
        self.sma25.append(df["sma25"])
        self.sma99.append(df["sma99"])

        self.bb_bbm.append(df["bb_bbm"])
        self.bb_bbh.append(df["bb_bbh"])
        self.bb_bbl.append(df["bb_bbl"])

        self.psar.append(df["psar"])

        self.MACD.append(df["MACD"])
        self.RSI.append(df["RSI"])

        # Add Simple Moving Average
        self.ax1.plot(date_render_range, self.sma7, '-')
        self.ax1.plot(date_render_range, self.sma25, '-')
        self.ax1.plot(date_render_range, self.sma99, '-')

        # Add Bollinger Bands
        self.ax1.plot(date_render_range, self.bb_bbm, '-')
        self.ax1.plot(date_render_range, self.bb_bbh, '-')
        self.ax1.plot(date_render_range, self.bb_bbl, '-')

        # Add Parabolic Stop and Reverse
        self.ax1.plot(date_render_range, self.psar, '.')

        self.ax4.clear()
        # Add Moving Average Convergence Divergence
        self.ax4.plot(date_render_range, self.MACD, 'r-')

        # Add Relative Strength Index
        self.ax4.plot(date_render_range, self.RSI, 'g-')

    # def render(self, date, open, high, low, close, volume, net_worth, trades):
    def render(self, df, net_worth, trades):
        """
        Render the environment to the screen
        :param df:
        :param net_worth:
        :param trades:
        :return:
        """
        date = df["Date"]
        open = df["Open"]
        high = df["High"]
        low = df["Low"]
        close = df["Close"]
        volume = df["Volume"]

        # Append volume & net_worth to deque list
        self.volume.append(volume)
        self.net_worth.append(net_worth)

        # Before appending to deque list, need to convert date to special format
        date = mpl_dates.date2num([pd.to_datetime(date)])[0]
        self.render_data.append([date, open, high, low, close])

        # Clear the frame rendered last step
        self.ax1.clear()
        candlestick_ohlc(self.ax1, self.render_data, width=0.8/24, colorup='green', colordown='red', alpha=0.8)

        # Put all dates to one list & fill ax2 subplot with volume
        date_render_range = [i[0] for i in self.render_data]
        self.ax2.clear()
        self.ax2.fill_between(date_render_range, self.volume, 0)

        if self.show_indicators:
            self.plot_indicators(df, date_render_range)

        # Draw our net_worth graph on ax3 (shared with ax1) subplot
        self.ax3.clear()
        self.ax3.plot(date_render_range, self.net_worth, color="blue")

        # Beautify the x-labels (date format)
        self.ax1.xaxis.set_major_formatter(self.date_format)
        self.fig.autofmt_xdate()

        minimum = np.min(np.array(self.render_data)[:, 1:])
        maximum = np.max(np.array(self.render_data)[:, 1:])
        RANGE = maximum - minimum

        # Sort sell & buy orders, put arrows in appropiate order positions
        for trade in trades:
            trade_date = mpl_dates.date2num([pd.to_datetime(trade['Date'])])[0]
            if trade_date in date_render_range:
                if trade['type'] == 'buy':
                    high_low = trade['Low'] - RANGE * 0.02
                    ycoords = trade['Low'] - RANGE * 0.08
                    self.ax1.scatter(
                        trade_date, high_low,
                        c='green', label='green', s=120, edgecolors='none', marker="^",
                    )
                else:
                    high_low = trade['High'] + RANGE * 0.02
                    ycoords = trade['High'] + RANGE * 0.06
                    self.ax1.scatter(
                        trade_date, high_low,
                        c='red', label='red', s=120, edgecolors='none', marker="v"
                    )

                if self.show_reward:
                    try:
                        self.ax1.annotate(
                            '{0:.2f}'.format(trade['Reward']),
                            (trade_date - 0.02, high_low),
                            xytext=(trade_date - 0.02, ycoords),
                            bbox={'boxstyle': 'round', 'fc': 'w', 'ec': 'k', 'lw': 1},
                            fontsize="small",
                        )
                    except Exception as e:
                        # print("Exception occured =>", str(e))
                        logger.append("Exception occured in utils.render =>" + str(e))
                        pass

        # Set layers every step, because subplots are cleared every step
        self.ax2.set_xlabel('Date')
        self.ax1.set_ylabel('Price')
        self.ax3.set_ylabel('Balance')

        # I use tight_layout to replace plt.subplots_adjust above
        self.fig.tight_layout()

        """Display image with matplotlib - interrupting other tasks"""
        # # Show the graph without blocking the rest of the program
        # plt.ion()
        # plt.show(block=False)
        # # Necessary to view frames before they are unrendered
        # plt.pause(0.001)

        """Display image with OpenCV - NO interruption"""
        # Redraw the canvas
        self.fig.canvas.draw()
        # convert canvas to image
        img = np.fromstring(self.fig.canvas.tostring_rgb(), dtype=np.uint8, sep='')
        img = img.reshape(self.fig.canvas.get_width_height()[::-1] + (3,))

        # img is rgb, convert to opencv's default bgr
        image = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
        # image = rgb_to_lab(img)

        # display image with OpenCV or any operation you like
        cv2.imshow("Bitcoin Trading Bot", image)

        if cv2.waitKey(25) & 0xFF == ord("q"):
            cv2.destroyAllWindows()
            return


def plot_ohlc(df):
    """
    Plot OHLC & indicators for technical analysis
    :param df:
    :return:
    """
    df_original = df.copy()

    # Necessary convert to datetime
    df["Date"] = pd.to_datetime(df.Date)
    df["Date"] = df["Date"].apply(mpl_dates.date2num)

    df = df[['Date', 'Open', 'High', 'Low', 'Close', 'Volume']]

    # Style ‘ggplot’
    plt.style.use('ggplot')

    # figsize attribute allows us to specify the width & height of a figure in unit inches
    fig = plt.figure(figsize=(16, 8), num="Bitcoin Trading Bot")

    # Create top subplot for price axis
    ax1 = plt.subplot2grid((6, 1), (0, 0), rowspan=5, colspan=1)

    # Create bottom subplot for volume which shares its x-axis
    ax2 = plt.subplot2grid((6, 1), (5, 0), rowspan=1, colspan=1, sharex=ax1)

    candlestick_ohlc(ax1, df.values, width=0.8/24, colorup='green', colordown='red', alpha=0.8)
    ax1.set_ylabel('Price', fontsize=12)
    plt.xlabel('Date')
    plt.xticks(rotation=45)

    # Add Simple Moving Average
    ax1.plot(df["Date"], df_original['sma7'], '-')
    ax1.plot(df["Date"], df_original['sma25'], '-')
    ax1.plot(df["Date"], df_original['sma99'], '-')

    # Add Bollinger Bands
    ax1.plot(df["Date"], df_original['bb_bbm'], '-')
    ax1.plot(df["Date"], df_original['bb_bbh'], '-')
    ax1.plot(df["Date"], df_original['bb_bbl'], '-')

    # Add Parabolic Stop and Reverse
    ax1.plot(df["Date"], df_original['psar'], '.')

    # # Add Moving Average Convergence Divergence
    ax2.plot(df["Date"], df_original['MACD'], '-')

    # # Add Relative Strength Index
    ax2.plot(df["Date"], df_original['RSI'], '-')

    # Beautify the x-labels (Date format)
    ax1.xaxis.set_major_formatter(mpl_dates.DateFormatter('%y-%m-%d'))  # %H:%M:%S'))
    fig.autofmt_xdate()
    fig.tight_layout()

    plt.show()
