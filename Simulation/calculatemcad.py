import pandas as pd
import math


class calculateMCAD:
    @classmethod
    def getMCAD(data):
        ema26 = pd.ewma(data, span = 26)
        ema12 = pd.ewma(data, span = 12)
        ema09 = pd.ewma(data, span = 9)
        mcadline = ema12 - ema26
        mcadhistogram = mcadline-ema09
        print(mcadline)
        print(mcadhistogram)

        return mcadline

    @classmethod
    def sigmoid(x):
        return 1 / (1 + math.exp(-x))