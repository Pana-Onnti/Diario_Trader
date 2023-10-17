from flask import session
from datetime import datetime
from request import obtener_trades_cuenta

# Auxiliares.py module

def get_session_data():
    if 'access_token' in session and 'user_data' in session:
        access_token = session['access_token']
        user_data = session['user_data']
        email = user_data.get('Email')
        return {'access_token':access_token, 'user_data':user_data, 'email':email}
    return None, None, None

def format_trades(trades_list):
        formatted_trades = []
        for trade in trades_list:
            formatted_trade = {}
            for key, value in trade.items():
                if key == 'Fecha_Entrada' or key == 'Fecha_Salida':
                    formatted_trade[key] = datetime.fromisoformat(value).strftime('%d/%m/%Y %H:%M:%S')
                else:
                    formatted_trade[key] = value
            formatted_trades.append(formatted_trade)
        return formatted_trades

def trades():
    usuario = get_session_data()
    email = usuario['email']
    trades = obtener_trades_cuenta(email)
    # Creamos un id único para cada trade
    for idx, trade in enumerate(trades['respuesta'][0]):
        trade['id'] = idx+1
        
        # Cambiamos el valor de 'Estado' por un string
        if trade['Estado'] == 0:
            trade['Estado'] = 'Close'
        elif trade['Estado'] == 1:
            trade['Estado'] = 'Open'
            
        # Cambiamos el valor de 'Direccion' por un string
        if trade['Direccion'] == 0:
            trade['Direccion'] = 'SHORT'
        elif trade['Direccion'] == 1:
            trade['Direccion'] = 'LONG'
            
    return trades['respuesta'][0]

