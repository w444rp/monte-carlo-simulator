# src/qmc/data/loader.py
from datetime import date
import requests
import pandas as pd


BASE_URL = "https://api.binance.com/api/v3/klines"

today = date.today()
def load_historical_data(
    symbol: str,
    interval: str = "1d",
    start: str = "2023-01-01",
    end: str = '2026-01-01',
) -> pd.DataFrame:

    start_ms = int(pd.Timestamp(start, tz="UTC").timestamp() * 1000)
    end_ms = int(pd.Timestamp(end, tz="UTC").timestamp() * 1000)

    all_data = []
    current_start = start_ms

    while current_start < end_ms:

        params = {
            "symbol": symbol.upper(),
            "interval": interval,
            "startTime": current_start,
            "endTime": end_ms,
            "limit": 1000,
        }

        response = requests.get(
            BASE_URL,
            params=params,
            timeout=10,
        )

        response.raise_for_status()

        data = response.json()

        if not data:
            break

        all_data.extend(data)

        # Время открытия последней полученной свечи
        last_open_time = data[-1][0]

        # Переходим к следующей свече
        current_start = last_open_time + 1

    columns = [
        "open_time",
        "open",
        "high",
        "low",
        "close",
        "volume",
        "close_time",
        "quote_volume",
        "number_of_trades",
        "taker_buy_base_volume",
        "taker_buy_quote_volume",
        "ignore",
    ]

    df = pd.DataFrame(all_data, columns=columns)

    # Время
    df["open_time"] = pd.to_datetime(
        df["open_time"],
        unit="ms",
        utc=True
    )

    df["close_time"] = pd.to_datetime(
        df["close_time"],
        unit="ms",
        utc=True
    )

    # Числовые значения
    numeric_columns = [
        "open",
        "high",
        "low",
        "close",
        "volume",
        "quote_volume",
        "taker_buy_base_volume",
        "taker_buy_quote_volume",
    ]

    df[numeric_columns] = df[numeric_columns].astype(float)

    df["number_of_trades"] = df["number_of_trades"].astype(int)

    # Убираем возможные дубликаты
    df = df.drop_duplicates(subset="open_time")

    # Сортируем
    df = df.sort_values("open_time")

    # Индекс
    df = df.reset_index(drop=True)

    return df