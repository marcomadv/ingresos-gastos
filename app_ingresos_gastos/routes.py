from app_ingresos_gastos import app
from flask import render_template

@app.route("/")
def index():
    datos=[
        {'fecha':'01/02/2023',
        'concepto':'Ropa',
        'monto':'-150'},
        {'fecha':'01/03/2023',
        'concepto':'Salario',
        'monto':'1500'},
        {'fecha':'15/03/2023',
        'concepto':'Supermercado',
        'monto':'-200'}
        ]
    return render_template("index.html",data = datos, title="Lista")

@app.route("/new")
def create():
    return render_template("new.html", title="Registro",tipoAccion = "Registro", tipoBoton= "Guardar")

@app.route("/update")
def edite():
    return render_template("update.html", title="Actualizar",tipoAccion = "Actualización", tipoBoton="Editar" )

@app.route("/delete")
def remove():
    return render_template("delete.html", title="Eliminar")