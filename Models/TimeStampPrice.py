__author__ = 'raymond'


class TimeStampPrice:
    def __init__(self, datetime, high_price, low_price, last_price, volume):
        self.datetime = datetime
        self.high_price = high_price
        self.low_price = low_price
        self.last_price = last_price
        self.volume = volume