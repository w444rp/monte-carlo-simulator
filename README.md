# Monte Carlo Simulation

A Python-based Monte Carlo simulation project for modeling future asset prices using **Geometric Brownian Motion (GBM)**.

The project estimates statistical parameters from historical market data and uses them to generate thousands of possible future price paths. The resulting simulations can be analyzed using quantiles and probability distributions.

## Features

* Historical market data loading
* Estimation of drift and volatility
* Geometric Brownian Motion simulation
* Thousands of simulated price paths
* Quantile analysis
* Distribution analysis of simulated final prices
* Price-path visualization
* Interactive command-line interface
* Windows and macOS support

## Mathematical Model

The project uses the **Geometric Brownian Motion** model, which is commonly used as a simplified mathematical model for asset prices.

The stochastic differential equation is:

$$
dS_t = \mu S_t\,dt + \sigma S_t\,dW_t
$$

where:

* $S_t$ — asset price at time $t$
* $\mu$ — expected return (drift)
* $\sigma$ — volatility
* $dt$ — time increment
* $dW_t$ — Wiener process increment

The analytical solution of the GBM equation is:

$$
S_t = S_0
\exp\left(
\left(\mu - \frac{1}{2}\sigma^2\right)t
+ \sigma W_t
\right)
$$

For numerical simulation, the project uses discrete time steps:

$$
S_{t+\Delta t}
=
S_t
\exp
\left[
\left(
\mu-\frac{1}{2}\sigma^2
\right)\Delta t
+
\sigma\sqrt{\Delta t}Z
\right]
$$

where:

$$
Z \sim N(0,1)
$$

is a standard normally distributed random variable.

For every simulation, independent random values of $Z$ are generated, producing a different possible future price path.

## Parameter Estimation

The model parameters are estimated from historical closing prices.

First, logarithmic returns are calculated:

$$
r_t =
\ln
\left(
\frac{S_t}{S_{t-1}}
\right)
$$

The drift is estimated from the average return:

$$
\mu = \frac{1}{n}\sum_{t=1}^{n}r_t
$$

and volatility is estimated using the standard deviation:

$$
\sigma = \operatorname{std}(r_t)
$$

These parameters are then used by the GBM model to generate future price scenarios.

## Monte Carlo Simulation

The simulation generates a large number of possible future paths.

For example, if the user selects:

```text
10,000 simulations
```

the model generates 10,000 independent possible future price trajectories.

Each simulation starts from the latest historical price:

$$
S_0 = S_{\text{latest}}
$$

The final prices of all simulations can then be analyzed statistically.

## Quantile Analysis

The project calculates several quantiles of the simulated final prices:

* 10th percentile
* 25th percentile
* 50th percentile
* 75th percentile
* 90th percentile

For example, the 50th percentile is the median simulated final price.

If:

$$
Q_{50} = 120000
$$

then approximately 50% of simulated final prices are below $120,000 and approximately 50% are above it.

The simulations are also divided into ranges:

* Below Q10
* Q10–Q25
* Q25–Q50
* Q50–Q75
* Q75–Q90
* Above Q90

This provides a simple view of the distribution of possible future prices.

## Project Structure

```text
monte-carlo-simulation/
│
├── LICENSE
├── README.md
├── pyproject.toml
│
└── src/
    ├── cli.py
    ├── requirements.txt
    ├── data_test.py
    ├── test_gbm.py
    ├── visualize_gbm.py
    │
    └── mcs/
        ├── __init__.py
        │
        ├── data/
        │   ├── __init__.py
        │   └── loader.py
        │
        ├── models/
        │   ├── __init__.py
        │   └── gbm.py
        │
        └── statistics/
            ├── __init__.py
            ├── metrics.py
            └── quantiles.py
```

## Requirements

* Python 3.10+
* NumPy
* Pandas
* Matplotlib
* Python-dateutil
* Rich

The project uses `pyproject.toml` for package configuration and dependency management.

## Installation

### Windows

Clone the repository:

```powershell
git clone https://github.com/YOUR_USERNAME/monte-carlo-simulation.git
cd monte-carlo-simulation
```

Create a virtual environment:

```powershell
python -m venv .venv
```

Activate it:

```powershell
.venv\Scripts\activate
```

Install the project:

```powershell
python -m pip install -e .
```

Run the application:

```powershell
mcs
```

### macOS

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/monte-carlo-simulation.git
cd monte-carlo-simulation
```

Create a virtual environment:

```bash
python3 -m venv .venv
```

Activate it:

```bash
source .venv/bin/activate
```

Install the project:

```bash
python3 -m pip install -e .
```

Run the application:

```bash
mcs
```

## Usage

After starting the application:

```text
MONTE CARLO SIMULATION
Geometric Brownian Motion Simulation

Enter ticker: BTC-USD

For simulation enter a path value (100-10000): 10000
```

The program then:

1. Loads historical market data.
2. Calculates model parameters.
3. Runs the Monte Carlo simulation.
4. Calculates quantiles.
5. Calculates the distribution of final simulated prices.
6. Displays the simulated price paths.
7. Shows the resulting analysis.

## Example

A typical simulation can generate thousands of possible future price paths from the current asset price.

The visualization shows the uncertainty of future prices rather than predicting a single deterministic price.

The greater the number of simulations, the more detailed the estimated distribution becomes.

## Important Note

This project is intended for **educational and research purposes**.

The Geometric Brownian Motion model is a simplified representation of financial markets. Real asset prices do not necessarily follow GBM assumptions, and simulated results should not be interpreted as reliable predictions of future market prices.

This project is **not financial advice**.

## Technologies

* Python
* NumPy
* Pandas
* Matplotlib
* SciPy-style statistical methodology
* Rich
* Geometric Brownian Motion
* Monte Carlo methods

## License

This project is distributed under the license included in the `LICENSE` file.

## Version

Current version:

```text
v1.0.0
```
