from keys import *
from alpaca.data.requests import StockBarsRequest
from alpaca.data.timeframe import TimeFrame
from alpaca.data.historical.stock import StockHistoricalDataClient
from datetime import datetime
import pandas as pd

start = datetime(2015, 1, 1)
end = datetime(2023, 1, 1)

trading_client = StockHistoricalDataClient(api_key=API_KEY, secret_key=SECRET_KEY)

def get_price_hist(stock, start: datetime, end: datetime):

    request_params = StockBarsRequest(
        symbol_or_symbols=stock,
        timeframe=TimeFrame.Day,
        start=start,
        end=end
    )

    stock_hist = trading_client.get_stock_bars(request_params)
    df = stock_hist.df
    df.reset_index(inplace=True)
    df.drop(['volume', 'trade_count', 'vwap'],axis = 1, inplace=True)

    return df

market_data_spy = get_price_hist('SPY', start=start, end=end)
market_data_efa = get_price_hist('EFA', start=start, end=end)
market_data_bnd = get_price_hist('BND', start=start, end=end)
market_data_vnq = get_price_hist('VNQ', start=start, end=end)
market_data_gsg = get_price_hist('GSG', start=start, end=end)

df = pd.concat([market_data_spy, market_data_gsg, market_data_bnd, market_data_efa, market_data_vnq], axis=1)
print(df)