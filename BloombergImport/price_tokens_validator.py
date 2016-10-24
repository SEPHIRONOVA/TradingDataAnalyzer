from datetime import datetime, time

__author__ = 'raymond'


class PriceTokensValidator:
	def __init__(self):
		self.opening_time = time(9, 30, 0)
		self.closing_time = time(16, 0, 0)

	def is_valid(self, price_tokens):
		if not PriceTokensValidator._has_valid_prices(price_tokens):
			return False

		if not self._within_trading_hours(price_tokens):
			return False

		return True

	@staticmethod
	def _has_valid_prices(price_tokens):
		datetime_index = 0

		if price_tokens[datetime_index]:
			return True
		else:
			return False

	def _within_trading_hours(self, price_tokens):
		datetime_index = 0

		time_stamp = datetime.strptime(price_tokens[datetime_index], '%m/%d/%Y %H:%M').time()
		if self.opening_time <= time_stamp <= self.closing_time:
			return True
		else:
			return False
