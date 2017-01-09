import numpy as np
import math
from typing import List
from Models.daily_result import DailyResult
from Simulation.daily_result_evaluator import DailyResultEvaluator

__author__ = 'raymond'


class SharpRatio:
	def __init__(self, daily_results: List[DailyResult], daily_result_evaluator: DailyResultEvaluator):
		self.daily_results = daily_results
		self.daily_result_evaluator = daily_result_evaluator

	def calculate(self):
		num_of_days = len(self.daily_results)
		return_of_days = np.empty(num_of_days, dtype=float)

		for i, daily_result in enumerate(self.daily_results):
			return_of_days[i] = self.daily_result_evaluator.calculate_return_of_day(daily_result)

		sharp_ratio = return_of_days.mean() / return_of_days.std() * math.sqrt(num_of_days)

		return sharp_ratio
