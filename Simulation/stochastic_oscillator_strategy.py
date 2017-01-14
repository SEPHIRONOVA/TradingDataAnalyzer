from Simulation.stochastic_oscillator import StochasticOscillator
from Simulation.calculation_status import CalculationStatus
from Simulation.sign_function import SignFunction
from Simulation.market_snapshot import MarketSnapshot
from Simulation.stock_snapshot_helper import StockSnapshotHelper
from Simulation.simple_moving_average import Simple_Moving_Average
from Models.queue import Queue


__author__ = 'Albert'

class StochasticOscillatorStrategy:

    def __init__(self,total_capital, num_stocks,look_back_period,k_period,d_period):
        self.transaction_amount = total_capital / num_stocks
        self.high_total_data = []
        self.low_total_data = []
        self.fast_k_percent = []
        self.k_percent = []
        self.old_k_percent = []
        self.d_percent = []
        self.old_d_percent = []

        for count in range(num_stocks):
            self.high_total_data.append(Queue(look_back_period))
            self.low_total_data.append(Queue(look_back_period))
            self.fast_k_percent.append(Simple_Moving_Average(k_period))
            self.k_percent.append(Simple_Moving_Average(k_period))
            self.old_k_percent.append(CalculationStatus.Invalid)
            self.d_percent.append(Simple_Moving_Average(d_period))
            self.old_d_percent.append(CalculationStatus.Invalid)

    def notify(self, market_snapshot: MarketSnapshot):
        decisions = []

        dec_value = 0

        for i, stock_snapshot in enumerate(market_snapshot.stock_snapshots):
            stock_snapshot_helper = StockSnapshotHelper(stock_snapshot)

            close_price = stock_snapshot_helper.get_close_price()
            high = stock_snapshot_helper.get_high()
            low = stock_snapshot_helper.get_low()

            self.high_total_data.push(high)
            self.low_total_data.push(low)

            highestHigh = self.high_total_data.get_max()
            lowestLow = self.low_total_data.get_min()

            if self.close_total_data.isFull():
                current_fast_k = StochasticOscillator.evaluate(close_price,highestHigh,lowestLow)

                current_k_percent = self.k_percent.evaluate(current_fast_k)

                if current_k_percent == CalculationStatus.Invalid:
                    self.old_k_percent[i] = current_k_percent
                    continue
                else:
                    self.old_k_percent[i] = current_k_percent
                    current_d_percent = self.d_percent.evaluate(current_k_percent)

                    if current_d_percent == CalculationStatus.Invalid:
                        self.old_d_percent[i] = current_d_percent
                        continue
                    else:

                        dec_value = SignFunction(self.current_k_percent-self.current_d_percent)-SignFunction(self.old_k_percent[i]-self.old_d_percent[i])

                        self.old_d_percent[i] = current_d_percent

            if dec_value > 0:
                decisions.append((stock_snapshot.ticker, -self.transaction_amount))
            elif dec_value < 0:
                decisions.append((stock_snapshot.ticker, +self.transaction_amount))
            else:
                decisions = []


            return decisions




