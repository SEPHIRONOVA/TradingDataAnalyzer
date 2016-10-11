from typing import List, Dict
from Models.TimeStampPrice import TimeStampPrice

__author__ = 'raymond'


class StockHistoryRecord:
	def __init__(self, ticker_symbol: str):
		self.ticker_symbol = ticker_symbol
		self.history_prices = {'BID': [], 'ASK': []}

	def add_time_stamp_price(self, time_stamp_price: TimeStampPrice, price_type):
		if price_type == 'BID':
			self.history_prices['BID'].append(time_stamp_price)
		elif price_type == 'ASK':
			self.history_prices['ASK'].append(time_stamp_price)
