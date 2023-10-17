from flask import Flask ,request,redirect
from flask import render_template
from flask import url_for
from graficos import *
from request import *
import requests


app = Flask(__name__)

@app.route('/form')
def create():
     return render_template('grafico.html')

@app.route('/registro', methods=['POST'])
def registro():
    try:
        respuesta = registrar_usuario(request, requests)
        print (respuesta)

    except Exception as e:
        print(f'Error al registrar usuario: {e}')
    else:
        print('Usuario creado exitosamente.')
    return redirect('/') 

@app.route('/registro_cuenta', methods=['POST'])
def registro_cuenta():
    try:
        respuesta = registrar_cuenta_nueva(request, requests)
        print (respuesta)
    except Exception as e:
        print(f'Error al registrar cuenta: {e}')
        respuesta = None
    else:
        print('Cuenta creada exitosamente.')
    return redirect('/')

@app.route('/registro_trade', methods=['POST'])
def registro_trade():
    email = request.form['Email']
    trade_data = {key: request.form[key] for key in request.form if key != 'Email'}
    url = f'http://127.0.0.1:8000/trades/crear/?email={email}'
    response = requests.post(url=url, json=trade_data)
    try:
        response.raise_for_status()
    except Exception as e:
        print(f'Error al registrar el Trade: {e.response.json()["detail"]}')
    else:
        print('Trade creado exitosamente.')

    return redirect('/')
