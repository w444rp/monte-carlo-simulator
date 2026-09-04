from mcs.data.loader import load_historical_data
from mcs.statistics.metrics import estimate_paraments
from datetime import date

today = date.today()
df = load_historical_data(
    symbol = 'BTCUSDT',
    interval = '1d',
    start = '2023-01-01',
    end = f'{today}',
)

print('--LOADER--')
print(f'Value of bars: {len(df)}')
print(f'First date: {df['open_time'].iloc[0]}')
print(f'Last date: {df['open_time'].iloc[-1]}')



mu, sigma = estimate_paraments(df['close'])

print("\n=== METRICS ===")
print(f"S0:    {df['close'].iloc[-1]:.2f}")
print(f"mu:    {mu:.4f}")
print(f"sigma: {sigma:.4f}")