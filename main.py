from pathlib import Path
from arima_sarima import analyze_dataset, run_arima_sarima

if __name__ == "__main__":
    dataset = {
        'file': Path('./data/bcdata.sgs.22709_02.csv'),
        'name': 'Balança Comercial - Saldo Mensal',
        'unit': 'US$ milhões',
        'color': 'green'
    }

    df = analyze_dataset(dataset['file'], dataset['name'], dataset['unit'], dataset['color'])
    run_arima_sarima(df, dataset['name'])
