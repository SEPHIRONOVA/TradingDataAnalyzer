from typing import List
from Models.market_history import MarketHistory
from Models.stock_history_record import StockHistoryRecord
from BloombergImport.stock_history_record_normalizer import StockHistoryRecordNormalizer

__author__ = 'raymond'


class MarketHistoryNormalizer:
	@staticmethod
	def normalize(market_history: MarketHistory):
		for key, record in market_history.records.items():
			StockHistoryRecordNormalizer.normalize(record)

		stock_history_records = [stock_history_record for ticker_symbol, stock_history_record in market_history.records.items()]
		starting_date = MarketHistoryNormalizer._get_largest_starting_date(stock_history_records)

		for key, record in market_history.records.items():
			StockHistoryRecordNormalizer.remove_extra_days(record, starting_date)

	@staticmethod
	def _get_largest_starting_date(stock_history_records: List[StockHistoryRecord]):
		assert len(stock_history_records) >= 1

		earliest_date_by_price_type = MarketHistoryNormalizer._get_starting_date_by_price_type(stock_history_records)
		largest_starting_date = max(starting_date for type, starting_date in earliest_date_by_price_type.items())

		return largest_starting_date

	@staticmethod
	def _get_starting_date_by_price_type(stock_history_records: List[StockHistoryRecord]):
		assert len(stock_history_records) >= 1

		start_dates_by_price_type = [MarketHistoryNormalizer._get_start_date_by_price_type(stock_history_record) for stock_history_record in stock_history_records]
		starting_date_by_price_type = {price_type: max(start_date_by_price_type[price_type] for start_date_by_price_type in start_dates_by_price_type) for price_type in start_dates_by_price_type[0]}

		return starting_date_by_price_type

	@staticmethod
	def _get_start_date_by_price_type(stock_history_record: StockHistoryRecord):
		timestamp_index = 0
		start_date_by_price_type = { price_type: timestamp_prices[timestamp_index].datetime.date() for (price_type, timestamp_prices) in
							  stock_history_record.prices_by_type.items()}

		return start_date_by_price_type
