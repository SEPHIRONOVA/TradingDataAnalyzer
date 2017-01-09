import time
from Models.market_history import MarketHistory
from Simulation.market_snapshot import MarketSnapshot
from Simulation.market_snapshot_helper import MarketSnapshotHelper

__author__ = 'raymond'

'''
	Market implements Subject in the Observer Pattern
	1. Register observers
	2. Unregister observers
	3. Notify all observers
'''


class Market:
	def __init__(self, market_history: MarketHistory):
		self.market_history = market_history
		self.traders = []

	def start(self):
		old_date = None
		print('Starting Market simulation: ' + format(time.clock(), '.2f') + ' secs')

		for market_snapshot in self._get_market_snapshot():
			old_date = Market._print_when_day_pass(old_date, market_snapshot)
			self.notify_all(market_snapshot)

		print('Market simulation ended')
		print()

	def register(self, trader):
		if trader in self.traders:
			return

		self.traders.append(trader)

	def unregister(self, trader):
		if trader not in self.traders:
			return

		self.traders.remove(trader)

	def notify_all(self, market_snapshot):
		for trader in self.traders:
			trader.notify(market_snapshot)

	def get_num_stocks(self):
		return self.market_history.get_num_stocks()

	@staticmethod
	def _print_when_day_pass(old_date, market_snapshot):
		market_snapshot_helper = MarketSnapshotHelper(market_snapshot)

		if old_date is None:
			old_date = market_snapshot_helper.get_date()
		else:
			date = market_snapshot_helper.get_date()
			if date == old_date:
				return
			else:
				print('Processing date: ', str(date))
				old_date = date

		return old_date

	def _get_market_snapshot(self):
		stock_snapshot_generators = [stock_snapshot for stock_snapshot in [stock_history_record.get_next() for ticker, stock_history_record in self.market_history.records.items()]]

		for stock_snapshots in zip(*stock_snapshot_generators):
			yield MarketSnapshot(stock_snapshots)
