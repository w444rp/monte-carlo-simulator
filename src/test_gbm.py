from mcs.models.gbm import GBM
from mcs.statistics.metrics import estimate_paraments
from mcs.data.loader import load_historical_data
from datetime import date
from dateutil.relativedelta import relativedelta
import pandas as pd
import numpy as np



three_years_ago = date.today() - relativedelta(years=3)
today = date.today()
while True:
    try:
        symbol = str(input('Enter a ticker: '))

        df = load_historical_data(
            symbol = f'{symbol}',
            interval = '1d',
            start = f'{three_years_ago}',
            end = f'{today}',
        )
        if df is None or df.empty:
            raise ValueError('No data about that ticker')
        break
    except Exception as e:
        print('Incorrect ticker')

n = len(pd.bdate_range(start=three_years_ago, end=today))
mu, sigma = estimate_paraments(df['close'])
s0  = df['close'].iloc[-1]
t = 3



print(GBM(mu, sigma, t, s0, n))
