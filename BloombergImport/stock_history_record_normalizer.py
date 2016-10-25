from typing import List
from Models.stock_history_record import StockHistoryRecord
from Models.timestamp_price import TimeStampPrice
from BloombergImport.timestamp_price_builder import TimeStampPriceBuilder
from datetime import date, datetime, time, timedelta

__author__ = 'raymond'


class StockHistoryRecordNormalizer:
	@staticmethod
	def normalize(stock_history_record: StockHistoryRecord):
		StockHistoryRecordNormalizer._sort_by_datetime(stock_history_record)
		StockHistoryRecordNormalizer._fill_empty_timestamps(stock_history_record)

	@staticmethod
	def _fill_empty_timestamps(stock_history_record: StockHistoryRecord):
		total_days_count = StockHistoryRecordNormalizer._get_days(stock_history_record)

		for price_type, timestamp_prices in stock_history_record.prices_by_type.items():
			assert len(timestamp_prices) >= 1

			i = 0
			days_count = total_days_count[price_type]
			total_minutes_of_trading_day = int((16 - 9.5) * 60) + 1

			for day in range(0, days_count, 1):
				opening_time = time(9, 30, 0)
				curr_time = opening_time
				prev_datetime = timestamp_prices[i]
				prev_open_price = -1.0
				prev_high_price = -1.0
				prev_low_price = -1.0
				prev_last_price = -1.0
				prev_volume = -1.0

				for minutes_passed in range(0, total_minutes_of_trading_day, 1):
					curr_time = StockHistoryRecordNormalizer._add_minutes(opening_time, minutes_passed)

					if i > len(timestamp_prices) - 1:
						prev_datetime = datetime.combine(prev_datetime.date(), curr_time)
						new_timestamp_price = TimeStampPrice(
							prev_datetime, prev_open_price, prev_high_price, prev_low_price, prev_last_price, prev_volume)
						timestamp_prices.insert(i, new_timestamp_price)
					elif curr_time == timestamp_prices[i].datetime.time():
						prev_datetime = timestamp_prices[i].datetime
						prev_open_price = timestamp_prices[i].open_price
						prev_high_price = timestamp_prices[i].high_price
						prev_low_price = timestamp_prices[i].low_price
						prev_last_price = timestamp_prices[i].last_price
						prev_volume = timestamp_prices[i].volume
					else:
						prev_datetime = datetime.combine(prev_datetime.date(), curr_time)
						new_timestamp_price = TimeStampPrice(
							prev_datetime, prev_open_price, prev_high_price, prev_low_price, prev_last_price, prev_volume)
						timestamp_prices.insert(i, new_timestamp_price)

					i += 1

				print('hello')

	@staticmethod
	def _get_days(stock_history_record: StockHistoryRecord):
		total_days_count = {}

		for price_type, timestamp_prices in stock_history_record.prices_by_type.items():
			distinct_days = set(timestamp_price.datetime.date() for timestamp_price in timestamp_prices)
			total_days_count[price_type] = len(distinct_days)

		return total_days_count

	@staticmethod
	def _sort_by_datetime(stock_history_record: StockHistoryRecord):
		for keys, prices in stock_history_record.prices_by_type.items():
			prices.sort(key=lambda p: p.datetime)

	@staticmethod
	def _add_minutes(curr_time, additional_minutes):
		return (datetime.combine(date.today(), curr_time) + timedelta(minutes=additional_minutes)).time()
