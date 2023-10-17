from flask import Flask ,request,redirect,flash,url_for,session, flash
from flask import render_template
from graficos import *
from request import *
import requests
from flask import redirect
from datetime import datetime
from auxiliares import get_session_data
##
from flask import session
from datetime import datetime
from request import obtener_trades_cuenta


#auxiliares.py module 
def get_session_data():
    if 'access_token' in session and 'user_data' in session:
        access_token = session['access_token']
        user_data = session['user_data']
        email = user_data.get('Email')
        return {'access_token':access_token, 'user_data':user_data, 'email':email}
    return None, None, None


import requests
from typing import Optional,Dict,Any
# usuario.py module
def get_access_token(username: str, password: str) -> Optional[str]:
    token_url = "http://127.0.0.1:8000/jwtauth/token/"
    data = {
        "grant_type": "password",
        "username": username,
        "password": password,
        "scope": "OAuth2PasswordBearer",
    }
    response = requests.post(token_url, data=data)
    if response.status_code == 200:
        access_token = response.json()["access_token"]
        return access_token
    else:
        print("Error al obtener el token de acceso:", response.text)
        return None 

def get_user_data(access_token: str) -> Optional[Dict[str, Any]]:
    api_url = "http://127.0.0.1:8000/jwtauth/me/"
    headers = {"Authorization": f"Bearer {access_token}"}
    response = requests.get(api_url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print("Error al obtener los datos de la API:", response.text)
        return None

def get_user_email(username: str, password: str) -> Optional[str]:
    access_token = get_access_token(username, password)

    if access_token is not None:
        user_data = get_user_data(access_token)

        if user_data is not None:
            return user_data.get("Email")

    return None

# main app module 
app = Flask(__name__)

user_loged = False
app.secret_key = 'my_secret_key'
@app.route('/')
def home():
    try:
        email = get_session_data()['email']
        access_token = get_session_data()['access_token']
        if access_token is not None:
            return render_template('index.html', email=email)
                                          
    except:
        return redirect(url_for('login'))


