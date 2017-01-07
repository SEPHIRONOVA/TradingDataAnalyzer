#!/usr/bin/env python

from Models.market_history import MarketHistory
from BloombergImport.bloomberg_data_reader import BloombergDataReader
from Simulation.market import Market
from Simulation.trader import Trader
from Simulation.vanilla_mcad_strategy import VanillaMcadStrategy
from Simulation.simulation_visualizer import SimulationVisualizer
from datetime import date

__author__ = 'raymond'

if __name__ == '__main__':
	capital_per_stock = 100000

	market_history = BloombergDataReader.load_bloomberg_trading_data('Resources/TSX60 Testing Trading Data(BID).csv',
																	 'Resources/TSX60 Testing Trading Data(ASK).csv')
	print()
	print()
	market = Market(market_history)

	num_of_stocks = market.get_num_stocks()
	trader = Trader(VanillaMcadStrategy(capital_per_stock * num_of_stocks, num_of_stocks), capital_per_stock * num_of_stocks)

	market.register(trader)
	market.start()
