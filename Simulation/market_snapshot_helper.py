from math import floor
from Simulation.market_snapshot import MarketSnapshot
from Simulation.stock_snapshot_helper import StockSnapshotHelper

__author__ = 'raymond'


class MarketSnapshotHelper:
	def __init__(self, market_snapshot: MarketSnapshot):
		self.market_snapshot = market_snapshot

	def convert_capital_to_shares(self, ticker, amount):
		assert amount > 0

		stock_snapshot = self._find_stock_snapshot_by_ticker(ticker)
		stock_snapshot_helper = StockSnapshotHelper(stock_snapshot)
		mid_price = stock_snapshot_helper.get_mid_price()
		num_shares = floor(amount / mid_price)
		extra_capital = amount - num_shares * mid_price
		return num_shares, extra_capital

	def convert_shares_to_capital(self, ticker, num_shares):
		stock_snapshot = self._find_stock_snapshot_by_ticker(ticker)
		stock_snapshot_helper = StockSnapshotHelper(stock_snapshot)
		mid_price = stock_snapshot_helper.get_mid_price()
		amount = mid_price * num_shares

		return amount

	def is_end_of_trading_hours(self):
		first_stock_snapshot = self.market_snapshot.stock_snapshots[0]
		stock_snapshot_helper = StockSnapshotHelper(first_stock_snapshot)

		return stock_snapshot_helper.is_end_of_trading_hours()

	def get_timestamp(self):
		first_stock_snapshot = self.market_snapshot.stock_snapshots[0]
		stock_snapshot_helper = StockSnapshotHelper(first_stock_snapshot)

		return stock_snapshot_helper.get_timestamp()

	def get_date(self):
		first_stock_snapshot = self.market_snapshot.stock_snapshots[0]
		stock_snapshot_helper = StockSnapshotHelper(first_stock_snapshot)

		return stock_snapshot_helper.get_date()

	def _find_stock_snapshot_by_ticker(self, ticker):
		return next(filter(lambda stock_snapshot: stock_snapshot.ticker == ticker, self.market_snapshot.stock_snapshots))
