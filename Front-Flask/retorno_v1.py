import plotly.express as px
import pandas as pd
import plotly.io as pio
import plotly.graph_objects as go

import plotly.express as px
import plotly.io as pio


def retornos():
    df = px.data.stocks(indexed=True) - 1
    df['total_value'] = df.sum(axis=1)
    df = df[1:]
    df['daily_return'] = df['total_value'].pct_change()
    df = df[1:]

    # Calcular el retorno diario

    # Calcular el retorno acumulado y el Total Return
    df['cumulative_return'] = (1 + df['daily_return']).cumprod() - 1
    df['total_return'] = df['cumulative_return'].iloc[-1]

    # Mostrar el DataFrame
    return  df['cumulative_return']

