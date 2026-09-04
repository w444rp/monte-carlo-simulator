# Monte Carlo Simulation

A Python project for simulating possible future asset prices using the **Monte Carlo method** and **Geometric Brownian Motion (GBM)**.

Historical market data is obtained from the **Binance API** and used to estimate the parameters required for the simulation.

## Mathematical Model

The asset price is modeled using the Geometric Brownian Motion stochastic differential equation:

$$
dS_t = \mu S_t\,dt + \sigma S_t\,dW_t
$$

where:

* $S_t$ — asset price at time $t$
* $\mu$ — drift
* $\sigma$ — volatility
* $dt$ — time increment
* $dW_t$ — Wiener process increment

The analytical solution is:

$$
S_t = S_0 e^{(\mu - \frac{\sigma^2}{2})t + \sigma W_t}
$$

For numerical simulation:

$$
S_{t+\Delta t} =
S_t e^{(\mu - \frac{\sigma^2}{2})\Delta t + \sigma\sqrt{\Delta t}Z_t}
$$

where:

$$
Z_t \sim N(0,1)
$$

## Parameter Estimation

Historical closing prices are converted into logarithmic returns:

$$
r_t = \ln\left(\frac{S_t}{S_{t-1}}\right)
$$

The drift is estimated as the mean of historical logarithmic returns:

$$
\mu = \frac{1}{n}\sum_{t=1}^{n} r_t
$$

Volatility is estimated as the standard deviation of the returns:

$$
\sigma = std(r_t)
$$

The latest available market price is used as the initial price:

$$
S_0 = S_{\text{latest}}
$$

## Data Source

Market data is obtained from the **Binance API**.

Historical cryptocurrency market data is used to calculate logarithmic returns, drift, and volatility.

## Installation

### Windows

```powershell
git clone https://github.com/w444rp/monte-carlo-simulation.git
cd monte-carlo-simulation

python -m venv .venv
.venv\Scripts\activate

python -m pip install -e .
mcs
```

### macOS / Linux

```bash
git clone https://github.com/w444rp/monte-carlo-simulation.git
cd monte-carlo-simulation

python3 -m venv .venv
source .venv/bin/activate

python3 -m pip install -e .
mcs
```

## Technologies

* Python 3.10+
* NumPy
* Pandas
* Matplotlib
* Binance API
* Rich

## Author

**w444rp** 


***Ekziira**
