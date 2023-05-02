from app_ingresos_gastos import app
from flask import render_template,request, redirect
import csv
from datetime import date

@app.route("/")
def index():
    datos=[]
    #llamada al archivo
    fichero = open('data/movimientos.csv','r')
    #accediendo a cada registro del archivo y lo formatea
    csvReader = csv.reader(fichero,delimiter=",",quotechar='"')
    #recorrer el objeto csvReader y cargar cada registro en la lista datos
    for items in csvReader:
        datos.append(items)

    return render_template("index.html",data=datos,title="Lista")

@app.route("/new", methods=["GET","POST"])
def create():
    if request.method == "POST":

        errores = validateForm(request.form)
        if errores:
            return render_template("new.html", title="Registro",tipoAccion = "Registro", tipoBoton= "Guardar", error = errores,dataForm = request.form)

        else:
            #acceder al archivo y configurar para cargar un nuevo registro
            mifichero = open ('data/movimientos.csv','a')
            #llamar al metodo writer y configuramos el formato 
            lectura = csv.writer(mifichero,delimiter=',',quotechar='"')
            #registramos los datos recibidos 
            lectura.writerow([request.form['fecha'],request.form['concepto'],request.form['monto']])
            mifichero.close()
        return redirect ("/") 
    
    else:
        return render_template("new.html",title = "Registro", tipoBoton= "Guardar",dataForm = {})

@app.route("/update")
def edite():
    return render_template("update.html", title="Actualizar",tipoAccion = "Actualización", tipoBoton="Editar" )

@app.route("/delete")
def remove():
    return render_template("delete.html", title="Eliminar")

def validateForm(datosFormulario):
    errores = [] #crear lista para guardar errores
    hoy = date.today().isoformat() #capturo la fecha de hoy 
    if datosFormulario['fecha'] > hoy:
        errores.append("La fecha no puede ser mayor a la actual")
    if datosFormulario['concepto'] == "":
        errores.append("El concepto no puede estar vacio")
    if float(datosFormulario['monto']) <= 0.0 or datosFormulario['monto'] == '':
        errores.append("El monto debe ser mayor a 0 o distinto de vacio")
    
    return errores

        
    


