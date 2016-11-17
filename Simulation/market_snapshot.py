from typing import Tuple
from Simulation.stock_snapshot import StockSnapshot

__author__ = 'raymond'


class MarketSnapshot:
	def __init__(self, stock_snapshots: Tuple[StockSnapshot]):
		self.stock_snapshots = stock_snapshots
