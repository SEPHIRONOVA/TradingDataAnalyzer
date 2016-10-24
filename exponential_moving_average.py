from datetime import datetime


class ExponentialMovingAverage:
	def __init__(self, interval):
		self.multiplier = 2 / (interval + 1)
		self.previous_value = 0

	def get_current_value(self, price, datetime: datetime):
		if datetime.time().minute < 12:
			return 0
		elif datetime.time().minute == 12:
			return
		current_value = (price - self.previous_value) * self.multiplier + self.previous_value
		self.previous_value = current_value

		return current_value
