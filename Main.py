from BloombergDataReader import BloombergDataReader

__author__ = 'raymond'

if __name__ == '__main__':
	BloombergDataReader.load_bloomberg_trading_data('Resources/TSX60 Trading Data(BID).csv','Resources/TSX60 Trading Data(ASK).csv')
