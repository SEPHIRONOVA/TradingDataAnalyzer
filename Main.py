#!/usr/bin/env python
import time
from BloombergImport.bloomberg_data_reader import BloombergDataReader
from Simulation.market import Market
from Simulation.trader import Trader
from Simulation.mcad_zero_crossover_strategy import McadZeroCrossoverStrategy
from Simulation.mcad_signal_line_crossover_strategy import McadSignalLineCrossoverStrategy
from Simulation.daily_result_evaluator import DailyResultEvaluator
from Simulation.sharp_ratio import SharpRatio
from Simulation.stochastic_oscillator_strategy import StochasticOscillatorStrategy

__author__ = 'raymond'

if __name__ == '__main__':
	capital_per_stock = 100000

	market_history = BloombergDataReader.load_bloomberg_trading_data('Resources/TSX60 Trading Data(BID).csv',
																	 'Resources/TSX60 Trading Data(ASK).csv')
	market = Market(market_history)

	num_of_stocks = market.get_num_stocks()
	initial_capital = capital_per_stock * num_of_stocks

	#trader1 = Trader(McadSignalLineCrossoverStrategy(initial_capital, num_of_stocks), initial_capital)
	#trader2 = Trader(McadZeroCrossoverStrategy(initial_capital, num_of_stocks), initial_capital)
	trader3 = Trader(StochasticOscillatorStrategy(initial_capital, num_of_stocks,14,3,3,0.7,0.3), initial_capital)

	#market.register(trader1)
	#market.register(trader2)
	market.register(trader3)
	market.start()

	evaluator = DailyResultEvaluator(initial_capital)
	print('Calculating daily profit and Loss: ' + format(time.clock(), '.2f') + ' secs')
	#for daily_result in trader1.daily_results:
	#	PnL1 = evaluator.calculate_profit_and_loss(daily_result)
	#	print(daily_result.date)
	#	print(PnL1)
	#	print()

	#for daily_result in trader2.daily_results:
	#	PnL2 = evaluator.calculate_profit_and_loss(daily_result)
	#	print(daily_result.date)
	#	print(PnL2)
	#	print()

	for daily_result in trader3.daily_results:
		PnL3 = evaluator.calculate_profit_and_loss(daily_result)
		print(daily_result.date)
		print(PnL3)
		print()

	#sharp_ratio1 = SharpRatio(trader1.daily_results, evaluator).calculate()
	#sharp_ratio2 = SharpRatio(trader2.daily_results, evaluator).calculate()
	sharp_ratio3 = SharpRatio(trader3.daily_results, evaluator).calculate()

	#print('Sharp ratio for Signal Line: ', sharp_ratio1)
	#print('Sharp ratio for Center Line: ', sharp_ratio2)
	print('Sharp ratio for Stochastic Oscillator: ', sharp_ratio3)
