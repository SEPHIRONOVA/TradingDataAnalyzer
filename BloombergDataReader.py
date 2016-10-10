#!/usr/bin/env python
import csv
from Models.TimeStampPrice import TimeStampPrice

def load_bloomberg_trading_data(file_name):
    with open(file_name, 'r') as csv_file:
        reader = csv.reader(csv_file)

        ignore_header(reader)
        stock_ticker_index = extract_stock_tickers(next(reader))

        for row in reader:
            print row
            break


def ignore_header(reader):
    for i in range(0, 2):
        next(reader)


def extract_stock_tickers(tickers):
    index_and_tickers = {}

    for i, ticker in enumerate(tickers):
        if ticker:
            index_and_tickers[i] = tickers[i]

    return index_and_tickers


if __name__ == '__main__':
    load_bloomberg_trading_data('Resources\TSX60 Trading Data.csv')