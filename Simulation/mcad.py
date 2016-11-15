from Simulation.calculation_status import CalculationStatus
from Simulation.exponential_moving_average import ExponentialMovingAverage

__author__ = 'raymond'


class Mcad:
	ema12_constant = 12
	ema26_constant = 26

	def __init__(self):
		self.ema12 = ExponentialMovingAverage(Mcad.ema12_constant)
		self.ema26 = ExponentialMovingAverage(Mcad.ema26_constant)

	def evaluate(self, current_price):
		ema12_result = self.ema12.evaluate(current_price)
		ema26_result = self.ema26.evaluate(current_price)

		if ema12_result == CalculationStatus.Invalid or ema26_result == CalculationStatus.Invalid:
			return CalculationStatus.Invalid

		return ema12_result - ema26_result

	def reset(self):
		self.ema12.reset()
		self.ema26.reset()
