import numpy as np
import pandas as pd

def calculate_log_returns(prices: pd.Series)-> pd.Series:
    return np.log(prices/prices.shift(1)).dropna()

def estimate_paraments(
        prices: pd.Series,
        periods_per_year: int = 365,
) -> tuple[float, float]:

    returns = calculate_log_returns(prices)

    mu = returns.mean() * periods_per_year
    sigma = returns.std()*np.sqrt(periods_per_year)


    return mu, sigma

