#!/usr/bin/env python

from Models.market_history import MarketHistory
from BloombergImport.bloomberg_data_reader import BloombergDataReader
from Simulation.market import Market

__author__ = 'raymond'

if __name__ == '__main__':
	market_history = BloombergDataReader.load_bloomberg_trading_data('Resources/TSX60 Trading Testing Data(BID).csv',
																	 'Resources/TSX60 Trading Testing Data(ASK).csv')

	market = Market(market_history)

	print('hello world')