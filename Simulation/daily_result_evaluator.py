from Models.daily_result import DailyResult

__author__ = 'raymond'


class DailyResultEvaluator:
	def __init__(self, original_capital):
		self.original_capital = original_capital

	def calculate_profit_or_loss(self, daily_result: DailyResult):
		remaining_capital = daily_result.cash + daily_result.portfolio_summary.calculate_capital()
		profit_or_loss = remaining_capital - self.original_capital

		return profit_or_loss
