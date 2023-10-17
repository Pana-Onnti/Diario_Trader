import pandas as pd
import json

balance_inicial = 2000
import numpy as np
from datetime import datetime

with open('trades_usuario.json', 'r') as f:
    data = json.load(f)
def crear_datos_trade (trades) :
    # Crear un DataFrame a partir de la lista de trades
    df = pd.DataFrame(data)

    # Asegurarse de que los valores numéricos se almacenan como floats
    df = df.astype({'Precio_Entrada': float, 'Precio_Salida': float, 'Comision': float})
    # convertir las columnas de fecha a datetime
    df['Fecha_Entrada'] = pd.to_datetime(df['Fecha_Entrada'])
    df['Fecha_Salida'] = pd.to_datetime(df['Fecha_Salida'])

    # calcular la diferencia de tiempo en días
    df['Tiempo_en_mercado'] = (df['Fecha_Salida'] - df['Fecha_Entrada']).dt.days

    df['PyG'] = df['Precio_Salida'] - df['Precio_Entrada']
    df['Trade_Return'] = (df['Precio_Salida'] - df['Precio_Entrada']) / df['Precio_Entrada']
    df['Trade_Return'] = df['Trade_Return'] *100
    df['PGL_acumuladas'] = df['PyG'].cumsum()
    df['Total_Value'] = balance_inicial + df['PyG'].cumsum()
    df['total_return'] =  (df['Total_Value'].iloc[-1] -balance_inicial )/ balance_inicial
    df['total_return'] = df['total_return'] * 100
    df['WIN_LONG'] = np.where((df['Direccion'] == 1) & (df['Precio_Entrada'] < df['Precio_Salida']), 1, 0)
    df['WIN_SHORT'] = np.where((df['Direccion'] == 0) & (df['Precio_Entrada'] > df['Precio_Salida']), 1, 0)
    df['Cantidad_Acciones'] = 1
    return df 
