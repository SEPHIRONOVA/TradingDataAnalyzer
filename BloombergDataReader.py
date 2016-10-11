#!/usr/bin/env python
from TradingDataRowParser import TradingDataRowParser
from StockHistoryRecordBuilder import StockHistoryRecordBuilder
import csv
from Models.TimeStampPrice import TimeStampPrice

__author__ = 'raymond'


class BloombergDataReader:
	@classmethod
	def load_bloomberg_trading_data(cls, file_name):
		with open(file_name, 'r') as csv_file:
			reader = csv.reader(csv_file)

			cls.ignore_header(reader)
			index_and_tickers, spacing = cls.extract_stock_tickers(next(reader))
			cls.ignore_first_row_with_time_stamp(reader)

			trading_data_row_parser = TradingDataRowParser(spacing)
			stock_history_record_builder = StockHistoryRecordBuilder(index_and_tickers, spacing)

			for row in reader:
				prices_and_indexes_generator = trading_data_row_parser.split_by_ticker_symbol(row)
				stock_history_record_builder.add_prices_by_tickers(prices_and_indexes_generator)

			print('hello world')

	@classmethod
	def extract_stock_tickers(cls, tickers):
		reached_second_ticker = False
		spacing = 0
		index_and_tickers = {}

		for i, ticker in enumerate(tickers):
			if ticker:
				index_and_tickers[i] = tickers[i]
				if not reached_second_ticker and i > 0:
					spacing = i
					reached_second_ticker = True

		return index_and_tickers, spacing

	@classmethod
	def ignore_header(cls, reader):
		header_line_count = 2
		cls.ignore_rows(reader, header_line_count)

	@classmethod
	def ignore_first_row_with_time_stamp(cls, reader):
		first_row_with_time_stamp_count = 1
		cls.ignore_rows(reader, first_row_with_time_stamp_count)

	@classmethod
	def ignore_rows(cls, reader, count):
		for i in range(0, count):
			next(reader)
