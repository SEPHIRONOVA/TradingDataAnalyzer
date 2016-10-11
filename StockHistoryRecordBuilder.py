from typing import Dict
from Models.StockHistoryRecord import StockHistoryRecord
from TimeStampPriceBuilder import TimeStampPriceBuilder

__author__ = 'raymond'


class StockHistoryRecordBuilder:
	def __init__(self, index_and_tickers: Dict[int, str], spacing):
		self.stock_history_records = {}  # type: Dict[str, StockHistoryRecord]
		self.index_and_tickers = index_and_tickers
		self.time_stamp_price_builder = TimeStampPriceBuilder(index_and_tickers)

	def add_prices_by_tickers(self, prices_and_indexes_generator):
		for price_tokens, start_index in prices_and_indexes_generator:
			self._add_price_to_stock_history_record(price_tokens, start_index)

	def _add_price_to_stock_history_record(self, price_tokens, start_index):
		if not self.time_stamp_price_builder.is_valid(price_tokens):
			return

		time_stamp_price = self.time_stamp_price_builder.build(price_tokens)
		ticker = self._find_ticker_by_index(start_index)

		if not self._exist_stock_history_record(ticker):
			stock_history_record = StockHistoryRecord(ticker)
			self.stock_history_records[ticker] = stock_history_record

		# TODO: Handle Bid and ask
		self.stock_history_records[ticker].add_time_stamp_price(time_stamp_price, 'BID')

	def _find_ticker_by_index(self, index) -> str:
		assert index in self.index_and_tickers

		return self.index_and_tickers[index]

	def _exist_stock_history_record(self, ticker):
		if ticker in self.stock_history_records:
			return True
		else:
			return False
