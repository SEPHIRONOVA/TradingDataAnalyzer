import os
import matplotlib.pyplot as plt
import numpy as np
from Simulation.visualization_data import VisualizationData

__author__ = 'raymond'


class SimulationVisualizer:
	@staticmethod
	def save_visualization_data(date, visualization_data : VisualizationData):
		for ticker, info in visualization_data.info_by_ticker.items():
			SimulationVisualizer._save_plot(ticker, date, info['prices'], info['mcad_history'])

	@staticmethod
	def _save_plot(ticker_symbol, date, stock_prices, mcad_history):
		minutes_elapsed = np.arange(len(stock_prices))

		f, (ax1, ax2) = plt.subplots(2, sharex=True)

		plt.title(ticker_symbol + '--' + str(date))
		ax1.plot(minutes_elapsed, stock_prices, 'b', label='prices')
		ax2.plot(minutes_elapsed, mcad_history, 'r', label='mcad history')
		plt.xlabel('minutes elapsed')
		plt.ylabel('price')
		plt.legend(loc='upper center', shadow=True)

		sample_file_name = "".join([c for c in ticker_symbol if c.isalpha() or c.isdigit() or c==' ']).rstrip()
		script_dir = os.path.dirname(__file__)
		results_dir = os.path.join(script_dir, 'Results')
		results_dir = os.path.join(results_dir, str(date))
		results_path = os.path.join(results_dir, sample_file_name)

		if not os.path.isdir(results_dir):
			os.makedirs(results_dir)
		plt.savefig(results_path)
		plt.close()
