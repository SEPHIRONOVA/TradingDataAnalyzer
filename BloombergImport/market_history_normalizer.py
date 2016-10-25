from typing import List
from Models.stock_history_record import StockHistoryRecord

__author__ = 'raymond'

class MarketHistoryNormalizer:
	def __init__(self, market_history: List[StockHistoryRecord]):
		pass

	@staticmethod
	def _get_largest_starting_date(market_history: List[StockHistoryRecord]):
		assert len(market_history) >= 1

		earliest_date_by_price_type = MarketHistoryNormalizer._get_starting_date_by_price_type(market_history)
		largest_starting_date = max(starting_date for type, starting_date in earliest_date_by_price_type.items())

		return largest_starting_date

	@staticmethod
	def _get_starting_date_by_price_type(market_history: List[StockHistoryRecord]):
		assert len(market_history) >= 1

		start_dates_by_price_type = [MarketHistoryNormalizer._get_start_date_by_price_type(stock_history_record) for stock_history_record in market_history]
		starting_date_by_price_type = {price_type: max([start_date_by_price_type[price_type] for start_date_by_price_type in start_dates_by_price_type]) for price_type in start_dates_by_price_type[0]}

		return starting_date_by_price_type

	@staticmethod
	def _get_start_date_by_price_type(stock_history_record: StockHistoryRecord):
		start_date_by_price_type = {price_type: timestamp_prices[0].datetime.date() for (price_type, timestamp_prices) in
							  stock_history_record.prices_by_type.items()}

		return start_date_by_price_type
