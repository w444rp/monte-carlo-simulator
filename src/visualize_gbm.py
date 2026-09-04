import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from mcs.data.loader import load_historical_data
from mcs.statistics.metrics import estimate_paraments
from mcs.models.gbm import GBM
from datetime import date
from dateutil.relativedelta import relativedelta
import pandas as pd

three_years_ago = date.today() - relativedelta(years=3)
today = date.today()

while True:
    try:
        symbol = str(input('Enter a ticker: '))

        df = load_historical_data(
            symbol=f'{symbol}',
            interval='1d',
            start=f'{three_years_ago}',
            end=f'{today}'
        )

        if df is None or df.empty:
            raise ValueError('No data about that ticker')

        break
    except Exception as e:
        print(f'Error of ticker: / {symbol} / Сlient Error: Bad Request for url')
        print('Check ticker name')

t = 3
s0 = float(df['close'].iloc[-1])
n = len(pd.bdate_range(start=three_years_ago, end=today))
mu, sigma = estimate_paraments(df['close'])
n_paths = 10000

paths = GBM(mu, sigma, t, s0, n, n_paths)

start_date = pd.to_datetime(df['open_time'].iloc[-1])

dates = pd.date_range(
    start=start_date,
    periods=paths.shape[1],
    freq='D'
)

fig, ax = plt.subplots(figsize=(10, 5))

n_paths_to_plot = 100

for i in range(n_paths_to_plot):
    ax.plot(
        dates,
        paths[i],
        alpha=0.18,
        linewidth=1.0
    )

fig.canvas.manager.set_window_title(
    f'GBM Simulation - [{symbol}] [{three_years_ago}] - [{today}]'
)

ax.set_xlabel('Date')
ax.set_ylabel('Price (USD)')

ax.yaxis.set_major_formatter(
    ticker.StrMethodFormatter('${x:,.0f}')
)

ax.grid(True, alpha=0.4)

plt.xticks(rotation=45)
fig.tight_layout()
plt.show()
