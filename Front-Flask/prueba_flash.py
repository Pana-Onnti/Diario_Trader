from flask import Flask, render_template, request, flash, redirect, url_for

app = Flask(__name__)
app.secret_key = 'mi_clave_secreta'

@app.route('/')
def index():
    return render_template('prueba_flash.html')

@app.route('/contacto', methods=['GET', 'POST'])
def contacto():
    if request.method == 'POST':
        nombre = request.form['nombre']
        email = request.form['email']
        mensaje = request.form['mensaje']
        # Procesar el formulario y enviar el mensaje
        flash('¡Gracias por contactarnos! Te responderemos pronto.', 'success')
        return redirect(url_for('index'))
    return render_template('contacto.html')

if __name__ == '__main__':  
    app.run()
