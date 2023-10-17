import requests

from enviroments import path

# GETS
URL_API = path

def peticion_general_get (extra_path:str,dato=None):
    if dato is None : dato = ''
    url_peticion = path+extra_path+dato
    peticion = requests.get(url=url_peticion)
    status = peticion.status_code
    respuesta = peticion.json()
    return {'respuesta':respuesta ,'status':status}

#Usuarios


def usuarios_buscar_email (Email:str):
    extra_path = 'usuariosbuscar/'
    peticion = peticion_general_get(extra_path=extra_path,dato=Email)
    return peticion

def usuarios_buscar_nombre(nombre_usuario:str):
    extra_path = 'usuariosbuscar/'
    peticion = peticion_general_get(extra_path=extra_path,dato=nombre_usuario)
    return peticion


# Cuentas 



def buscar_cuenta_email(Email:str):
    extra_path = 'cuentas/buscar/'
    peticion = peticion_general_get(extra_path=extra_path,dato=Email)
    return peticion

def devolver_cuentas():
    extra_path = 'cuentas/cuentas'
    peticion = peticion_general_get(extra_path=extra_path)
    return peticion

#Trades


def devolver_trades():
    extra_path = 'trades/trades'
    peticion = peticion_general_get(extra_path=extra_path)
    return peticion


def obtener_trades_cuenta(Email:str):
    extra_path = 'trades/buscar/'
    peticion = peticion_general_get(extra_path=extra_path,dato=Email)
    return peticion


# POSTS

def crear_usuario(usuario, api):
    url = URL_API+'usuarios/crear/'
    respuesta_api = api.post(url=url, json=usuario)
    respuesta = respuesta_api.json()
    if 'detail' in respuesta:
        raise Exception(respuesta['detail'])
    return respuesta

def registrar_usuario(request, api):
    usuario_nuevo = {
        'Nombre': request.form['Nombre'],
        'Apellido': request.form['Apellido'],
        'User_name': request.form['User_name'],
        'Password': request.form['Password'],
        'Email': request.form['Email']
    }
    respuesta = crear_usuario(usuario_nuevo, api)
    return respuesta

##


def crear_cuenta(cuenta, email, api):
    url = URL_API+'cuentas/crear/'
    url_api = f'{url}?email={email}'
    respuesta_api = api.post(url=url_api, json=cuenta)
    respuesta = respuesta_api.json()
    if 'detail' in respuesta:
        raise Exception(respuesta['detail'])
    return respuesta
from auxiliares import get_session_data

def registrar_cuenta_nueva(request, api):
    email = get_session_data()['email']
    cuenta_nueva = {
        'Id_Estado': request.form['Id_Estado'],
        'Balance': request.form['Balance']
    }
    respuesta = crear_cuenta(cuenta_nueva, email, api)
    return respuesta



###


