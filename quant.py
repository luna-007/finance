import bt
import matplotlib.pyplot as plt 
# %matplotlib inline
from dataclasses import asdict

data = bt.get('aapl', start = '2020-01-01')  # type: ignore

# print(data.head())

strat = bt.Strategy('s1', [bt.algos.RunMonthly(),
                           bt.algos.SelectAll(),
                           bt.algos.WeighEqually(),
                           bt.algos.Rebalance()])

test = bt.Backtest(strat, data)

res = bt.run(test)

# plt.plot(res)
res.plot_histogram()
# plt.show()
