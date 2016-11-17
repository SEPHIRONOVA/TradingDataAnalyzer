import pandas as pd


class calculatemcad:
    @classmethod
    def getMCAD(data):
        ema26 = pd.ewma(data['price'], span = 26)
        ema12 = pd.ewma(data['price'], span = 12)
        ema09 = pd.ewma(data['price'], span = 9)
        mcadline = ema12 - ema26
        mcadhistogram = mcadline-ema09
        print(mcadline)
        print(mcadhistogram)

        return mcadline

    @classmethod
    def sigmoid(x):
        return 1 / (1 + math.exp(-x))