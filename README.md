# TradingDataAnalyzer

## Project Summary
This project is an implementation of day trading algorithms based on Momentum indicators. The projects consists of following components:
1. Core Algorithm component
2. Traders with different trading strategies/hyperparameters
a. MACD 
b. Stochastic Oscillator
3. Simulation systems to regist trader for comparison of different strategies

## Input Data Description
**Trading Universe:** Stocks in S&P/TSX 60 Index 
**Source:** Bloomberg Terminal
**Period:** 3/23/2016 to 9/30/2016

| Column | Description |
| ------ | ------ |
| TICKER | Ticker for stock |
| Time | Time of the price in mm/dd/yyyy:hh:mm format |
| OPEN | The price of stock at start of a minute |
| LAST | The price of stock at the end of a minute |
| HIGH | Highest price in the minute |
| LOW | Lowest price in the minute |
| VOLUME | Trading volume of price in the minute |

## Technical Indicators 

**Trading Indicators Used:** 

1. MACD: 
    - MACD Center-Line crossover
    - MACD Line: 15 period EMA of mid-price – 40 period EMA of mid-price
    - MACD Signal-Line crossover
    - MACD Line: 15 period of mid-price – 40 period of mid-price
    - Signal Line: 9 period EMA of MACD 

2. Stochastic Oscillator: 
    - Fast %K = (Current Close - Lowest Low)/(Highest High - Lowest Low)* 100
    - Full %K = Fast %K smoothed with X-period SMA
    - Full %D = X-period SMA of Full %K.
    Where: 
        Lowest Low = lowest low for the look-back period
        Highest High = highest high for the look-back period
        Upper bound for bearish signal: 80%
        Lower bound for bullish signal: 20%

Note: EMA – Exponential Moving Average, SMA- Simple Moving Average

## Trading Stategy

**- Bullish:**
When bullish signal identified, trader will change the position to long
    - MACD: MACD cross above the zero/signal line
    - Stochastic Oscillator: Oscillator value drops below lower bound
    
**- Bearish:** 
When bearish signal identified, trader will change the position to short
    - MACD: short amount when MACD cross below the zero/signal line
    - Stochastic Oscillator: Oscillator value grows above upper bound
    
Volume of trading = Trade until maximum net position reaches
Maximum net position = Absolute value of Position

e.g. When expected position change from short to long, trader will purchase stock with amount that will not only cover maximum position but also reach maximum long positon

## Authors:
- [SEPHIRONOVA](https://github.com/SEPHIRONOVA)
- [virtualraymond](https://github.com/virtualraymond)
- [HearttBreak](https://github.com/HearttBreaker)

## License
**MIT**
