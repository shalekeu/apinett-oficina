from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

def conectar_db():
    conn = sqlite3.connect('facturas.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def inicio():
    return render_template('index.html')

@app.route('/planes')
def planes():
    return render_template('planes.html')

@app.route('/nosotros')
def nosotros():
    return render_template('nosotros.html')

@app.route('/oficina-virtual')
def oficina():
    return render_template('oficina.html')

@app.route('/consultar', methods=['POST'])
def consultar():
    cedula = request.form.get('cedula')
    conn = conectar_db()
    resultado = conn.execute("SELECT * FROM clientes WHERE cedula = ?", (cedula,)).fetchone()
    conn.close()
    return render_template('oficina.html', factura=resultado, busqueda=True)

    if __name__ == '__main__':
    # Esto permite que el hosting asigne el puerto automáticamente
    app.run(host='0.0.0.0', port=5000)