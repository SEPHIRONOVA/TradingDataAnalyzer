from Models.portfolio_summary import PortfolioSummary
from Simulation.portfolio import Portfolio
from Simulation.market_snapshot_helper import MarketSnapshotHelper

__author__ = 'raymond'

class Trader:
	def __init__(self, trading_strategy, total_capital):
		self.strategy = trading_strategy
		self.total_capital_backup = total_capital
		self.total_capital = total_capital
		self.portfolio = Portfolio()
		self.portfolio_summaries = []

	def notify(self, market_snapshot):
		market_snapshot_helper = MarketSnapshotHelper(market_snapshot)
		if market_snapshot_helper.is_end_of_trading_hours():
			portfolio_summary = self.portfolio.evaluate(market_snapshot)
			self.portfolio_summaries.append(portfolio_summary)
			self.portfolio.clear()
			self.total_capital = self.total_capital_backup
			return

		decisions = self.strategy.notify(market_snapshot)

		if decisions is None:
			return

		for ticker, amount in decisions:
			if amount > 0:
				extra_capital = self.portfolio.buy(market_snapshot, ticker, amount)
				self.total_capital -= amount
				self.total_capital += extra_capital
			else:
				extra_capital = self.portfolio.short(market_snapshot, ticker, amount)
				self.total_capital += amount
				self.total_capital -+ extra_capital
