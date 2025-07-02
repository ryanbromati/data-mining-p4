import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA
from statsmodels.tsa.statespace.sarimax import SARIMAX
from scipy.stats import linregress

plt.style.use("seaborn-v0_8-whitegrid")
plt.rcParams['figure.figsize'] = (12, 8)

def load_bcb_data(file_path):
    df = pd.read_csv(file_path, delimiter=';')
    df["valor"] = df["valor"].astype(str).str.replace(",", ".", regex=False).astype(float)
    df["data"] = pd.to_datetime(df["data"], dayfirst=True)
    df = df.sort_values("data").reset_index(drop=True)
    return df

def calc_trend(series, threshold=0.01):
    x = np.arange(len(series))
    slope, intercept, r_value, _, _ = linregress(x, series)
    if slope > threshold:
        trend = "crescente"
    elif slope < -threshold:
        trend = "decrescente"
    else:
        trend = "estável"
    return trend, slope, intercept, r_value

def plot_series(ax, dates, values, slope, intercept, title, ylabel, color='blue'):
    ax.plot(dates, values, color=color, linewidth=1.5, alpha=0.7)
    ax.plot(dates, intercept + slope * np.arange(len(values)), "--", color='red', linewidth=2)
    ax.set_title(title)
    ax.set_ylabel(ylabel)
    ax.tick_params(axis='x', rotation=45)

def analyze_dataset(file_path, dataset_name, unit, color='blue'):
    df = load_bcb_data(file_path)
    df = df.set_index("data")
    df.index = pd.DatetimeIndex(df.index).to_period('M')
    trend, slope, intercept, r = calc_trend(df["valor"])
    print(f"• Tendência: {trend.upper()}, Inclinação: {slope:.4f}, R²: {r**2:.4f}")
    fig, ax = plt.subplots()
    plot_series(ax, df.index.to_timestamp(), df["valor"], slope, intercept, f"{dataset_name}", unit, color)
    plt.tight_layout()
    plt.show()
    return df


def run_arima_sarima(df, label):
    y = df["valor"]

    print(f"Rodando ARIMA e SARIMA para: {label}\n")

    # ARIMA
    model_arima = ARIMA(y, order=(1, 1, 1))
    result_arima = model_arima.fit()
    print("Resumo ARIMA:")
    print(result_arima.summary())
    forecast_arima = result_arima.forecast(steps=12)
    print("\nPrevisão ARIMA (12 meses):")
    print(forecast_arima)

    # SARIMA
    model_sarima = SARIMAX(y, order=(1, 1, 1), seasonal_order=(1, 1, 1, 12))
    result_sarima = model_sarima.fit(disp=False)
    print("\nResumo SARIMA:")
    print(result_sarima.summary())
    forecast_sarima = result_sarima.forecast(steps=12)
    print("\nPrevisão SARIMA (12 meses):")
    print(forecast_sarima)

    # Gráfico (mantém)
    plt.figure(figsize=(14, 6))
    y.plot(label="Série Original", linewidth=1)
    forecast_arima.plot(label="ARIMA (12 meses)", linestyle="--")
    forecast_sarima.plot(label="SARIMA (12 meses)", linestyle=":")
    plt.title(f"Previsão ARIMA e SARIMA - {label}")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()
