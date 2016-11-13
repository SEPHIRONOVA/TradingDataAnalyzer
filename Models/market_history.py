from typing import Dict
from Models.stock_history_record import StockHistoryRecord

__author__ = 'raymond'


class MarketHistory:
	def __init__(self, market_history_records: Dict[str, StockHistoryRecord]):
		self.records = market_history_records
