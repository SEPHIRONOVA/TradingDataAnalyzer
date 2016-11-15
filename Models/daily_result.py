from Models.portfolio_summary import PortfolioSummary

__author__ = 'raymond'


class DailyResult:
	def __init__(self, date, cash, portfolio_summary: PortfolioSummary):
		self.date = date
		self.cash = cash
		self.portfolio_summary = portfolio_summary
