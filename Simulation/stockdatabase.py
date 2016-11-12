import datetime
import pandas as pd

class stockdatabase:
    def __init__(self):
        #self.CurDate = CurDate

        #curyear = self.CurDate.year()
        #curmonth = self.CurDate.month()
        #curdate = self.CurDate.month()

        #starttime = datetime._build_struct_time(curyear,curmonth,curdate, 9, 30, 0, 0)
        #endtime = datetime._build_struct_time(curyear, curmonth, curdate, 16, 0, 0, 0)
        #total_period = int((16 - 9.5) * 60) + 1
        #index = pd.date_range(starttime,endtime,periods=total_period,freq='M')
        column = ['time','price']
        self.stockprice = pd.DataFrame(columns = column)
        #print(self.stockprice)
        #self.stockprice.fillna()

    def add_time_price(curtime,curprice):
        toappend = pd.DataFrame([[curtime,curprice]], columns=['time','price'])
        #print(toappend)
        stockdatabase.stockprice = stockdatabase.stockprice.append(toappend,ignore_index = True)
        #print(stockdatabase.stockprice)

    def gettail(x):
        return stockdatabase.stockprice.tail(x)

    def print(self):
        print(stockdatabase.stockprice)

