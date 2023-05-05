from app_ingresos_gastos import app, LAST_ID_FILE, MOVIMIENTOS_FILE
from flask import render_template,request, redirect
import csv
from datetime import date

@app.route("/")
def index():
    datos=[]
    #llamada al archivo
    fichero = open(MOVIMIENTOS_FILE,'r')
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

            ##################################### Generar el nuevo Id en el registro ######################################

            fichero = open(LAST_ID_FILE,'r')
            last_id = fichero.read()
            if last_id == '':
                new_id = 1
            else:
                new_id = int(last_id) +1
            
            fichero.close()


            ####################################### Guardar el nuevo last_id ########################################
            fichero = open(LAST_ID_FILE,'w')
            fichero.write(str(new_id))
            fichero.close()

            #acceder al archivo y configurar para cargar un nuevo registro
            mifichero = open (MOVIMIENTOS_FILE,'a')
            #llamar al metodo writer y configuramos el formato 
            lectura = csv.writer(mifichero,delimiter=',',quotechar='"')
            
             #registramos los datos recibidos
            lectura.writerow([new_id,request.form['fecha'],request.form['concepto'],request.form['monto']])
            mifichero.close()
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

        mificheroDelete = open(MOVIMIENTOS_FILE,'r')
        lectura = csv.reader(mificheroDelete, delimiter=',',quotechar='"')
        registro_buscado=[]
        for registros in lectura:
            if registros[0] == str(id):
                #aqui encuentro el id buscado en mi registro
                registro_buscado.append(registros)

        return render_template("delete.html", title="Eliminar", data=registro_buscado)

    else:
        #aqui seria el metodo http post
        ##########lectura del archivo para listar los registros excepto el del id dado###### 
        fichero_read = open(MOVIMIENTOS_FILE,'r')
        csvReader = csv.reader(fichero_read,delimiter=',',quotechar='"')

        registro_buscado=[]
        for registros in csvReader:
            if registros[0] != str(id):
                #guardamos todos menos el registro con el id para borrar
                registro_buscado.append(registros)

        fichero_read.close()
        ######guardar el registro obtenido#######
        fichero_save = open(MOVIMIENTOS_FILE,'w', newline='')
        csvWriter = csv.writer(fichero_save, delimiter=',',quotechar='"')
        for datos in registro_buscado:
            csvWriter.writerow(datos)
        fichero_save.close()

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

        
    


