from typing import List
from typing import Dict
from Models.target_exposure import TargetExposure

__author__ = 'raymond'


class PortfolioSummary:
	def __init__(self, profit_by_ticker: Dict[str, float], target_exposures_by_ticker: Dict[str, List[TargetExposure]]):
		self.profit_by_ticker = profit_by_ticker
		self.target_exposures_by_ticker = target_exposures_by_ticker
