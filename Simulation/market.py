from typing import List
from Models.market_history import MarketHistory
from Simulation.market_snapshot import MarketSnapshot

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

	def proceed(self):
		pass

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

	def _get_market_snapshot(self):
		stock_snapshot_generators = [stock_snapshot for stock_snapshot in [stock_history_record.get_next() for ticker, stock_history_record in self.market_history.records.items()]]

		for stock_snapshots in zip(*stock_snapshot_generators):
			yield MarketSnapshot(stock_snapshots)
