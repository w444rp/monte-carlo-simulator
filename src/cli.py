import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import pandas as pd

from datetime import date
from dateutil.relativedelta import relativedelta
from rich.console import Console
from rich.panel import Panel
from rich.progress import track
from rich.table import Table

from mcs.data.loader import load_historical_data
from mcs.statistics.metrics import estimate_paraments
from mcs.models.gbm import GBM
from mcs.statistics.quantiles import calculate_distribution, calculate_quantiles

console = Console()

today = date.today()
three_years_later = date.today()-relativedelta(years=3)

def main():
    console.print(
        Panel.fit(
            "[bold]MONTE CARLO SIMULATION[/bold]\n"
            "Geometric Brownian Motion Simulation",
            border_style="blue"
        )
    )

    while True:
        try:
            console.print(' ')
            console.print(' ')
            console.print(' ')
            symbol = str(console.input('Enter [bold]ticker[/bold]:'))

            df = load_historical_data(
                symbol = f'{symbol}',
                interval = '1d',
                start = f'{three_years_later}',
                end = f'{today}'
            )

            if df is None or df.empty:
                raise ValueError(console.print('[bold red]Error:[/bold red] No data about that ticker'))

            break
        except Exception as e:
            console.print(' ')
            console.print(' ')
            console.print('[bold red]Error of ticker name[/bold red]\n'
            'Check ticker name')
    console.print('[bold green]Historical data loaded[/bold green]')


    t = 3
    s0 = float(df['close'].iloc[-1])
    n = len(pd.bdate_range(start=three_years_later, end=today))
    mu, sigma = estimate_paraments(df['close'])

    while True:
        try:
            console.print(' ')
            n_paths = int(console.input('[bold]For simulation enter a path value (100-10000): [/bold]'))
            console.print(' ')
            

            if n_paths>=10_001 or n_paths<100:
                console.print('[bold red]Too match paths[/bold red]')
                continue
            break
        except ValueError:
            console.print('')
            console.print('[bold red]Enter a number[/bold red]')
            console.print('')

    

    with console.status('[bold blue]Running Monte Carlo Simulation...[/bold blue]'):
        console.print('')
        paths = GBM(mu, sigma, t, s0, n, n_paths)
        console.print('')

    start_date = pd.to_datetime(df['open_time'].iloc[-1])

    quantiles = calculate_quantiles(paths)
    distribution = calculate_distribution(paths)

    table = Table(title='Price Quantiles')

    table.add_column('Quantile')
    table.add_column('Price', justify='right')

    for quantile, price in quantiles.items():
        table.add_row(
            quantile,
            f'${price:,.2f}'
        )
    console.print(table)


    table_d = Table(title='Simulator Disrtibution')

    table_d.add_column('Price Range')
    table_d.add_column('Simulations', justify='right')
    table_d.add_column('Share', justify='right')

    for range_name, data in distribution.items():
        table_d.add_row(
            range_name, 
            f'{data['count']:,}',
            f'{data['percentage']:.2f}%'
        )

    console.print(table_d)


    dates = pd.date_range(
        start = start_date,
        periods = paths.shape[1],
        freq='D'
    )
    
    console.print('[bold]Opening visualization...[/bold]')


    fig, ax = plt.subplots(figsize=(10,5))

    for i in range(n_paths):
        ax.plot(
            dates,
            paths[i],
            alpha = 0.18,
            linewidth = 1.0
        )

    fig.canvas.manager.set_window_title(
        f'GBM Simulation - [{symbol}]  [{three_years_later}] - [{today}]'
    )

    ax.set_xlabel('Date')
    ax.set_ylabel('Price (USD)')

    ax.yaxis.set_major_formatter(
        ticker.StrMethodFormatter('${x:,.0f}')
    )

    ax.grid(True, alpha = 0.4)

    plt.xticks(rotation = 45)
    fig.tight_layout()
    plt.show()



if __name__ =='__main__':
    main()