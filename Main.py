#!/usr/bin/env python
from BloombergImport.bloomberg_data_reader import BloombergDataReader

__author__ = 'raymond'

if __name__ == '__main__':
	BloombergDataReader.load_bloomberg_trading_data('Resources/TSX60 Trading Testing Data(BID).csv',
													'Resources/TSX60 Trading Testing Data(ASK).csv')
