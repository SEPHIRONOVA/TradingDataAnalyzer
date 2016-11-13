import csv
import time

from Models.market_history import MarketHistory
from BloombergImport.trading_data_row_parser import TradingDataRowParser
from BloombergImport.stock_history_record_builder import StockHistoryRecordBuilder
from BloombergImport.stock_history_record_normalizer import StockHistoryRecordNormalizer
from BloombergImport.market_history_normalizer import MarketHistoryNormalizer

__author__ = 'raymond'


class BloombergDataReader:
	@classmethod
	def load_bloomberg_trading_data(cls, bid_data_file, ask_data_file) -> MarketHistory:
		print('Start reading data sheet')
		print(time.clock())
		stock_history_record_builder = StockHistoryRecordBuilder()
		cls._load_single_data_sheet(bid_data_file, 'BID', stock_history_record_builder)
		cls._load_single_data_sheet(ask_data_file, 'ASK', stock_history_record_builder)
		print('data sheet fully loaded')
		print(time.clock())

		print('start sanitizing market data')
		stock_history_records = stock_history_record_builder.stock_history_records
		market_history = MarketHistory(stock_history_records)
		MarketHistoryNormalizer.Normalize(market_history)
		print(time.clock())
		print('data sanitization completed')

		return market_history

	@classmethod
	def _load_single_data_sheet(cls, data_file, price_type, stock_history_record_builder):
		with open(data_file, 'r') as csv_file:
			reader = csv.reader(csv_file)

			cls._ignore_header(reader)
			index_and_tickers, spacing = cls._extract_stock_tickers(next(reader))
			cls._ignore_first_row_with_time_stamp(reader)

			trading_data_row_parser = TradingDataRowParser(spacing)
			stock_history_record_builder.setup(index_and_tickers, spacing)

			for row in reader:
				prices_and_indexes = trading_data_row_parser.split_by_ticker_symbol(row)
				stock_history_record_builder.add_prices_by_tickers(prices_and_indexes, price_type)

	@classmethod
	def _extract_stock_tickers(cls, tickers):
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
	def _ignore_header(cls, reader):
		header_line_count = 2
		cls._ignore_rows(reader, header_line_count)

	@classmethod
	def _ignore_first_row_with_time_stamp(cls, reader):
		first_row_with_time_stamp_count = 1
		cls._ignore_rows(reader, first_row_with_time_stamp_count)

	@classmethod
	def _ignore_rows(cls, reader, count):
		for i in range(0, count):
			next(reader)
