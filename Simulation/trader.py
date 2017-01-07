from Models.portfolio_summary import PortfolioSummary
from Models.daily_result import DailyResult
from Simulation.portfolio import Portfolio
from Simulation.market_snapshot_helper import MarketSnapshotHelper
from Simulation.daily_result_evaluator import DailyResultEvaluator
from Simulation.simulation_visualizer import SimulationVisualizer

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
			self.daily_results.append(daily_result)
			self.portfolio.clear()
			visualization_data = self.strategy.reset()
			SimulationVisualizer.save_visualization_data(market_snapshot_helper.get_date(), visualization_data)

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
			daily_p_l.append(self.daily_result_evaluator.calculate_profit_or_loss(daily_result))

		return daily_p_l
