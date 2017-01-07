__author__ = 'raymond'


class VisualizationData:
	def __init__(self):
		self.info_by_ticker = {}

	def add_price(self, ticker_symbol, price):
		if ticker_symbol not in self.info_by_ticker:
			self.info_by_ticker[ticker_symbol] = {'prices': [], 'mcad_history': []}

		self.info_by_ticker[ticker_symbol]['prices'].append(price)

	def add_mcad(self, ticker_symbol, mcad):
		if ticker_symbol not in self.info_by_ticker:
			self.info_by_ticker[ticker_symbol] = []

		self.info_by_ticker[ticker_symbol]['mcad_history'].append(mcad)
