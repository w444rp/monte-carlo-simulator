import numpy as np


def GBM (
        mu: float,
        sigma: float,
        t: float,
        s0:float,
        n:float,
        n_simulations: int = 10000
):
    dt = t/n
    z = np.random.standard_normal(size=(n_simulations, n))

    increments = (
        (mu - 0.5*sigma**2)*dt + sigma*np.sqrt(dt)*z
    )

    log_paths = np.cumsum(increments, axis=1)

    paths = s0*np.exp(log_paths)

    paths = np.column_stack(
        [np.full(n_simulations, s0), paths]

    )

    return paths


