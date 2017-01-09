from typing import List
from datetime import date, datetime, time, timedelta
from Models.target_exposure import TargetExposure
from Models.daily_result import DailyResult
from Models.portfolio_summary import PortfolioSummary

__author__ = 'raymond'


class DailyResultEvaluator:
	opening_time = time(9, 30, 0)
	total_trading_minutes = int((16 - 9.5) * 60) + 1

	def __init__(self, original_capital):
		self.original_capital = original_capital

	def calculate_return_of_day(self, daily_result: DailyResult):
		total_profit_and_loss = self.calculate_profit_and_loss(daily_result)
		maximum_sum_of_exposure = max(DailyResultEvaluator.calculate_sum_of_capital_exposure_by_ticker(daily_result.portfolio_summary).values())

		return_of_day = total_profit_and_loss / maximum_sum_of_exposure

		return return_of_day

	def calculate_profit_and_loss(self, daily_result: DailyResult):
		remaining_capital = daily_result.cash + DailyResultEvaluator.calculate_portfolio_worth(daily_result.portfolio_summary)
		profit_or_loss = remaining_capital - self.original_capital

		return profit_or_loss

	@staticmethod
	def calculate_sum_of_capital_exposure_by_ticker(portfolio_summary: PortfolioSummary):
		exposure_sum_by_ticker = {}

		for ticker, target_exposures in portfolio_summary.target_exposures_by_ticker.items():
			exposure_sum = DailyResultEvaluator._calculate_sum_of_capital_exposure(target_exposures)
			exposure_sum_by_ticker[ticker] = exposure_sum

		return exposure_sum_by_ticker

	@staticmethod
	def calculate_portfolio_worth(portfolio_summary: PortfolioSummary):
		return sum(portfolio_summary.profit_by_ticker.values())

	@staticmethod
	def _calculate_sum_of_capital_exposure(target_exposures: List[TargetExposure]):
		opening_time = time(9, 30, 0)
		curr_exposure = 0
		exposure_sum = 0
		i = 0

		for minutes_passed in range(0, DailyResultEvaluator.total_trading_minutes, 1):
			curr_time = DailyResultEvaluator._add_minutes(opening_time, minutes_passed)
			if i < len(target_exposures) and curr_time == target_exposures[i].timestamp.time():
				curr_exposure += target_exposures[i].amount
				i += 1

			exposure_sum += curr_exposure

		return exposure_sum

	@staticmethod
	def _add_minutes(curr_time, additional_minutes):
		return (datetime.combine(date.today(), curr_time) + timedelta(minutes=additional_minutes)).time()
