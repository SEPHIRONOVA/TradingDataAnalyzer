__author__ = 'raymond'


class TradingDataRowParser:
	def __init__(self, spacing):
		self.spacing = spacing

	def split_by_ticker_symbol(self, row):
		for ticker_start_index in range(0, len(row), self.spacing):
			yield row[ticker_start_index:ticker_start_index + self.spacing], ticker_start_index
