from Models.target_exposure import TargetExposure
from Models.portfolio_summary import PortfolioSummary
from Simulation.market_snapshot import MarketSnapshot
from Simulation.market_snapshot_helper import MarketSnapshotHelper

__author__ = 'raymond'


class Portfolio:
	def __init__(self):
		self.shares_by_ticker = {}
		self.target_exposures = []

	def short(self, market_snapshot: MarketSnapshotHelper, ticker, amount):
		market_snapshot_helper = MarketSnapshotHelper(market_snapshot)
		num_shares, extra_capital = market_snapshot_helper.convert_capital_to_shares(ticker, amount)
		used_amount = amount - extra_capital
		timestamp = market_snapshot_helper.get_timestamp()
		self._update_capital_exposure(timestamp, ticker, used_amount)

		if self._has_ticker(ticker):
			self.shares_by_ticker[ticker] -= num_shares
		else:
			self.shares_by_ticker[ticker] = -num_shares

		return extra_capital

	def buy(self, market_snapshot, ticker, amount):
		market_snapshot_helper = MarketSnapshotHelper(market_snapshot)
		num_shares, extra_capital = market_snapshot_helper.convert_capital_to_shares(ticker, amount)
		used_amount = amount - extra_capital
		timestamp = market_snapshot_helper.get_timestamp()
		self._update_capital_exposure(timestamp, ticker, used_amount)

		if self._has_ticker(ticker):
			self.shares_by_ticker[ticker] += num_shares
		else:
			self.shares_by_ticker[ticker] = num_shares

		return extra_capital

	def evaluate(self, market_snapshot):
		market_snapshot_helper = MarketSnapshotHelper(market_snapshot)
		profit_by_ticker = {ticker: market_snapshot_helper.convert_shares_to_capital(ticker, share) for ticker, share in self.shares_by_ticker.items()}

		return PortfolioSummary(profit_by_ticker, self.target_exposures)

	def clear(self):
		self.shares_by_ticker.clear()
		self.target_exposures.clear()

	def _update_capital_exposure(self, timestamp, ticker, used_amount):
		self.target_exposures.append(TargetExposure(timestamp, ticker, used_amount))

	def _has_ticker(self, ticker):
		if ticker in self.shares_by_ticker:
			return True
		else:
			return False
