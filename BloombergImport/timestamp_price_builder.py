from typing import Dict
from datetime import datetime

from Models.timestamp_price import TimeStampPrice
from BloombergImport.price_tokens_validator import PriceTokensValidator

__author__ = 'raymond'


class TimeStampPriceBuilder:
	def __init__(self, index_and_tickers: Dict[int, str]):
		self.index_and_tickers = index_and_tickers
		self.price_token_validator = PriceTokensValidator()

	def build(self, price_tokens):
		assert self.price_token_validator.is_valid(price_tokens)

		datetime_index = 0
		open_price_index = 1
		high_price_index = 2
		low_price_index = 3
		last_price_index = 4
		volume_index = 5

		tokens = price_tokens[datetime_index].split()
		date_tokens = tokens[0].split('/')
		time_tokens = tokens[1].split(':')
		time_stamp = datetime(int(date_tokens[2]), int(date_tokens[0]), int(date_tokens[1]), int(time_tokens[0]), int(time_tokens[1]))
		#time_stamp = datetime.strptime(price_tokens[datetime_index], '%m/%d/%Y %H:%M')
		time_stamp = datetime.strptime(price_tokens[datetime_index], '%m/%d/%Y %H:%M')
		open_price = float(price_tokens[open_price_index])
		high_price = float(price_tokens[high_price_index])
		low_price = float(price_tokens[low_price_index])
		last_price = float(price_tokens[last_price_index])
		volume = int(price_tokens[volume_index])
		time_stamp_price = TimeStampPrice(time_stamp, open_price, high_price, low_price, last_price, volume)

		return time_stamp_price
