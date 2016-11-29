from typing import Dict
from Models.portfolio_summary import PortfolioSummary
from Models.daily_result import DailyResult
from Simulation.portfolio import Portfolio
from Simulation.market_snapshot_helper import MarketSnapshotHelper
from Simulation.daily_result_evaluator import DailyResultEvaluator

__author__ = 'raymond'

class Trader:
	def __init__(self, trading_strategy, total_capital):
		self.total_capital_backup = total_capital
		self.total_capital = total_capital
		self.strategy = trading_strategy
		self.portfolio = Portfolio()
		self.daily_results = []
		self.daily_result_evaluator = DailyResultEvaluator(total_capital)

	def notify(self, market_snapshot):
		market_snapshot_helper = MarketSnapshotHelper(market_snapshot)
		if market_snapshot_helper.is_end_of_trading_hours():
			date = market_snapshot_helper.get_date()
			portfolio_summary = self.portfolio.evaluate(market_snapshot)
			daily_result = DailyResult(date, self.total_capital, portfolio_summary)

			print("\n")
			print("The end of day")
			print(daily_result.date)
			#for Target_exposure in daily_result.portfolio_summary.target_exposures:
			#	print(Target_exposure.ticker)
			#	print(Target_exposure.amount)

			#print("Finish printing target_exposures for today")


			self.daily_results.append(daily_result)

			print("Start printing today's profit/loss")

			print(self.calculate_daily_profit_loss())
			print("\nTotal profit/loss so far:")
			print(sum(self.calculate_daily_profit_loss()))
			#for c in self.calculate_daily_profit_loss():
			#	print(c)

			print("Finish printing today's profit/loss")

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



	def calculate_daily_profit_loss(self):
		daily_p_l = list()
		for daily_result in self.daily_results:
			daily_p_l.append(DailyResultEvaluator.calculate_profit_or_loss(self.daily_result_evaluator,daily_result))

		return daily_p_l


	#def calculate_daily_exposure(self):
	#    for daily_result in self.daily_results
	#        for Target_exposure in daily_result.portfolio_summarytarget_exposures:
	#            for ticker in Target_exposure.ticker
	#