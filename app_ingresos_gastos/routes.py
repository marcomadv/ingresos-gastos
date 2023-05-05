from app_ingresos_gastos import app, LAST_ID_FILE, MOVIMIENTOS_FILE
from flask import render_template,request, redirect
import csv
from datetime import date
from app_ingresos_gastos.models import *


@app.route("/")
def index():
    datos = select_all()
    return render_template("index.html",data=datos,title="Lista")

@app.route("/new", methods=["GET","POST"])
def create():
    if request.method == "POST":

        errores = validateForm(request.form)
        if errores:
            return render_template("new.html", title="Registro",tipoAccion = "Registro", tipoBoton= "Guardar", error = errores,dataForm = request.form)

        else:
            insert(request.form)
        return redirect ("/")
    
    else:
        return render_template("new.html",title = "Registro", tipoBoton= "Guardar",dataForm = {})

@app.route("/update/<int:id>", methods =["GET","POST"])
def edit(id):
    if request.method == 'GET':
        mificheroUpdate = open(MOVIMIENTOS_FILE,'r')
        lectura = csv.reader(mificheroUpdate, delimiter=',',quotechar='"')
        registro_buscado=[]
        for registros in lectura:
            if registros[0] == str(id):
                #aqui encuentro el id buscado en mi registro
                registro_buscado=registros
        return render_template("update.html", title="Actualizar",tipoAccion = "Actualización", tipoBoton="Editar",dataForm=registro_buscado)

    else:
        #aqui entra el post
        return f"aqui debo actualizar los datos con el registro dado id:{id}"
    
@app.route("/delete/<int:id>", methods = ["GET","POST"])
def remove(id):

    if request.method == "GET":

    #1.Consultar en data/movimientos.csv y recuperar el registro con el id de la peticion
    #2.Devolver al formulario html una previsualizacion para luego borrarlo definitivamente con un boton

        registro_buscado = select_by(id,True)
        return render_template("delete.html", title="Eliminar", data=registro_buscado)

    else:
        #aqui seria el metodo http post
        ##########lectura del archivo para listar los registros excepto el del id dado###### 
        registro_buscado = select_by(id,False)
        ######guardar el registro obtenido#######
        delete_by(registro_buscado)
        
    return redirect("/")

#Funcion para validar formulario de registro donde controlemos los input con algunos requisitos:
def validateForm(datosFormulario):
    errores = [] #crear lista para guardar errores
    hoy = date.today().isoformat() #capturo la fecha de hoy 
    if datosFormulario['fecha'] > hoy:
        errores.append("La fecha no puede ser mayor a la actual")
    if datosFormulario['concepto'] == "":
        errores.append("El concepto no puede estar vacio")
    if float(datosFormulario['monto']) == 0.0 or datosFormulario['monto'] == '':
        errores.append("El monto debe ser mayor a 0 o distinto de vacio")
    
    return errores

        
    


