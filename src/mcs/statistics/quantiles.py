import numpy as np

def calculate_quantiles(paths):
    final_prices = paths[:, -1]

    quantiles = {
        '10%': np.quantile(final_prices, 0.10),
        '25%': np.quantile(final_prices, 0.25),
        '50%': np.quantile(final_prices, 0.50),
        '75%': np.quantile(final_prices, 0.75),
        '90%': np.quantile(final_prices, 0.90)
    }

    return quantiles

def calculate_distribution(paths):
    final_prices = paths[:, -1]

    q10 = np.quantile(final_prices, 0.10)
    q25 = np.quantile(final_prices, 0.25)
    q50 = np.quantile(final_prices, 0.50)
    q75 = np.quantile(final_prices, 0.75)
    q90 = np.quantile(final_prices, 0.90)

    total = len(final_prices)

    distribution = {
        'Below Q10': np.sum(final_prices <= q10),
        'Q10-Q25': np.sum((final_prices>q10)&(final_prices<=q25)),
        'Q25-Q50': np.sum((final_prices>q25)&(final_prices<=q50)),
        'Q50-Q75': np.sum((final_prices>q50)&(final_prices<=q75)),
        'Q75-Q90': np.sum((final_prices>q75)&(final_prices<=q90))
    }

    result = {}

    for key, count in distribution.items():
        result[key] = {
            'count': int(count),
            'percentage': float(count/total * 100)
        }

    return result

