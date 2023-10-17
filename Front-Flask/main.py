from flask import Flask ,request,redirect,flash,url_for,session, flash
from flask import render_template
from graficos import *
from request import *
import requests
from flask import redirect
from usuario import get_user_email,get_access_token,get_user_data
from datetime import datetime
from auxiliares import get_session_data,trades,format_trades
##

##
# crear la logica de etl de los datos para los graficos y aplicarlos 
##
app = Flask(__name__)

user_loged = False
app.secret_key = 'my_secret_key'
#redirect general 
@app.errorhandler(404)
def page_not_found(e):
    return redirect(url_for('home'))

#

@app.route('/cuentas')
def cuentas_vista():
    email  = get_session_data()['email']
    nota = buscar_cuenta_email(email)
    cuentas = nota['respuesta']['cuentas']
    print (cuentas)
    return render_template('cuenta.html',cuentas=cuentas,email=email)

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
    return redirect(url_for('cuentas_vista'))


#ruta principal 
@app.route('/')
def home():
    try:
        email = get_session_data()['email']
        access_token = get_session_data()['access_token']
        if access_token is not None:
            try:
                grafico_area  = generar_grafico_area()
                grafico_pie = generar_grafico_pie()
                long_bar_chart = generate_long_bar_chart()
                dif_bar_chart= generate_dif_bar_chart()
            except:
                pass

        return render_template('index.html', email=email,
                                graph=grafico_area,
                                graph1=generar_grafico_area(),
                                graph2=generar_grafico_area(),
                                graph3=grafico_pie,
                                graph4=long_bar_chart,
                                graph5=dif_bar_chart)
                
    except:
        return redirect(url_for('login'))




#login 

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['usuario']
        password = request.form['password']
        access_token = get_access_token(username, password)
        if access_token is not None:
            user_data = get_user_data(access_token)
            session['access_token'] = access_token
            session['user_data'] = user_data
            return redirect(url_for('home'))
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('access_token', None)
    return redirect(url_for('login'))
#
import json
# vistas GET
@app.route('/trades')
def trades_vista():
    trades_usuario = trades()
    trades_usuario = format_trades(trades_usuario)
    email = get_session_data()['email']
    # casero test
    #with open('trades_usuario.json', 'w') as archivo:
    #    json.dump(trades_usuario, archivo)
    print (email)
    return render_template('trades1.html',email=email,trades=trades_usuario)


@app.route('/registro')
def registro_vista():
     return render_template('registro.html')



# registros  POST 
@app.route('/registro', methods=['POST'])
def registro_usuario():
    try:
        respuesta = registrar_usuario(request, requests)
        print (respuesta)

    except Exception as e:
        mensaje = 'Error al registrar usuario: {e}'
        print(f'Error al registrar usuario: {e}')
    else:
        mensaje = 'Usuario creado correctamente '
        print('Usuario creado exitosamente.')
    
    return redirect(url_for('home'))

@app.route('/registro_trade', methods=['POST'])
def registro_trade():
    mensaje = 'onnti'
    email =  get_session_data()['email'] #request.form['Email']
    trade_data = {key: request.form[key] for key in request.form if key != 'Email' }
    trade_data['Estado'] = '1'
    url = f'http://127.0.0.1:8000/trades/crear/?email={email}'
    response = requests.post(url=url, json=trade_data)
    try:
        response.raise_for_status()
    except Exception as e:
        mensaje = f'Error al registrar el Trade: {e.response.json()["detail"]}'
        print(f'Error al registrar el Trade: {e.response.json()["detail"]}')
    else:
        mensaje = 'Trade creado exitosamente.'
        print('Trade creado exitosamente.')
        return redirect(url_for('trades_vista'))
    
    return render_template('trades1.html' , mensaje = mensaje)




