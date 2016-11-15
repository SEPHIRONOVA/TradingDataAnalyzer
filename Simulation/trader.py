from Models.portfolio_summary import PortfolioSummary
from Models.daily_result import DailyResult
from Simulation.portfolio import Portfolio
from Simulation.market_snapshot_helper import MarketSnapshotHelper

__author__ = 'raymond'


class Trader:
	def __init__(self, trading_strategy, total_capital):
		self.total_capital_backup = total_capital
		self.total_capital = total_capital
		self.strategy = trading_strategy
		self.portfolio = Portfolio()
		self.daily_results = []

	def notify(self, market_snapshot):
		market_snapshot_helper = MarketSnapshotHelper(market_snapshot)
		if market_snapshot_helper.is_end_of_trading_hours():
			date = market_snapshot_helper.get_date()
			portfolio_summary = self.portfolio.evaluate(market_snapshot)
			daily_result = DailyResult(date, self.total_capital, portfolio_summary)
			self.daily_results.append(daily_result)
			self.portfolio.clear()
			self.strategy.reset()
			self.total_capital = self.total_capital_backup
			return

		decisions = self.strategy.notify(market_snapshot)

		for ticker, amount in decisions:
			if amount > 0:
				extra_capital = self.portfolio.buy(market_snapshot, ticker, amount)
				self.total_capital -= amount
				self.total_capital += extra_capital
			elif amount < 0:
				extra_capital = self.portfolio.short(market_snapshot, ticker, -amount)
				self.total_capital += amount
				self.total_capital -= extra_capital
			else:
				print('DEBUG: Should never happen')
				assert False
