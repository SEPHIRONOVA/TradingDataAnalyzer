#!/usr/bin/env python
from BloombergImport.bloomberg_data_reader import BloombergDataReader
from Simulation import stockdatabase,calculatemcad
import pandas as pd

__author__ = 'raymond'

#if __name__ == '__main__':
#	BloombergDataReader.load_bloomberg_trading_data('Resources/TSX60 Trading Data(BID).csv',
#													'Resources/TSX60 Trading Data(ASK).csv')

stockdatabase.stockdatabase.__init__(stockdatabase)
stockdatabase.stockdatabase.add_time_price(stockdatabase,'2016-10-20,0:9:30:0',23.46)
stockdatabase.stockdatabase.add_time_price(stockdatabase,'2016-10-20,0:9:31:0',23.46)
stockdatabase.stockdatabase.add_time_price(stockdatabase,'2016-10-20,0:9:32:0',23.46)
stockdatabase.stockdatabase.add_time_price(stockdatabase,'2016-10-20,0:9:33:0',23.46)
stockdatabase.stockdatabase.add_time_price(stockdatabase,'2016-10-20,0:9:34:0',23.46)
stockdatabase.stockdatabase.add_time_price(stockdatabase,'2016-10-20,0:9:35:0',23.46)
stockdatabase.stockdatabase.add_time_price(stockdatabase,'2016-10-20,0:9:36:0',23.46)
stockdatabase.stockdatabase.add_time_price(stockdatabase,'2016-10-20,0:9:37:0',23.46)
stockdatabase.stockdatabase.add_time_price(stockdatabase,'2016-10-20,0:9:38:0',23.46)
stockdatabase.stockdatabase.add_time_price(stockdatabase,'2016-10-20,0:9:39:0',23.46)
stockdatabase.stockdatabase.add_time_price(stockdatabase,'2016-10-20,0:9:40:0',23.46)
stockdatabase.stockdatabase.add_time_price(stockdatabase,'2016-10-20,0:9:41:0',23.46)
stockdatabase.stockdatabase.add_time_price(stockdatabase,'2016-10-20,0:9:42:0',23.46)
stockdatabase.stockdatabase.add_time_price(stockdatabase,'2016-10-20,0:9:43:0',23.46)
stockdatabase.stockdatabase.add_time_price(stockdatabase,'2016-10-20,0:9:44:0',23.46)
stockdatabase.stockdatabase.add_time_price(stockdatabase,'2016-10-20,0:9:45:0',23.46)
stockdatabase.stockdatabase.add_time_price(stockdatabase,'2016-10-20,0:9:46:0',23.46)
stockdatabase.stockdatabase.add_time_price(stockdatabase,'2016-10-20,0:9:47:0',23.46)
stockdatabase.stockdatabase.add_time_price(stockdatabase,'2016-10-20,0:9:48:0',23.46)
stockdatabase.stockdatabase.add_time_price(stockdatabase,'2016-10-20,0:9:49:0',23.46)
stockdatabase.stockdatabase.add_time_price(stockdatabase,'2016-10-20,0:9:50:0',23.46)
stockdatabase.stockdatabase.add_time_price(stockdatabase,'2016-10-20,0:9:51:0',23.46)
stockdatabase.stockdatabase.add_time_price(stockdatabase,'2016-10-20,0:9:52:0',23.46)
stockdatabase.stockdatabase.add_time_price(stockdatabase,'2016-10-20,0:9:53:0',23.46)
stockdatabase.stockdatabase.add_time_price(stockdatabase,'2016-10-20,0:9:54:0',23.46)
stockdatabase.stockdatabase.add_time_price(stockdatabase,'2016-10-20,0:9:55:0',23.46)
stockdatabase.stockdatabase.add_time_price(stockdatabase,'2016-10-20,0:9:56:0',23.46)
stockdatabase.stockdatabase.add_time_price(stockdatabase,'2016-10-20,0:9:57:0',23.46)
stockdatabase.stockdatabase.add_time_price(stockdatabase,'2016-10-20,0:9:58:0',23.46)
stockdatabase.stockdatabase.add_time_price(stockdatabase,'2016-10-20,0:9:59:0',23.46)

price = stockdatabase.stockprice.price.tail(26)

mcad = calculatemcad.getMCAD(price)
#print(mcad)


