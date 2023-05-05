from app_ingresos_gastos import *
import csv



def select_all():
    datos=[]
    #llamada al archivo
    fichero = open(MOVIMIENTOS_FILE,'r')
    #accediendo a cada registro del archivo y lo formatea
    csvReader = csv.reader(fichero,delimiter=",",quotechar='"')
    #recorrer el objeto csvReader y cargar cada registro en la lista datos
    for items in csvReader:
        datos.append(items)
    fichero.close()

    return datos

    
def select_by(id, condicion):
    mificheroDelete = open(MOVIMIENTOS_FILE,'r')
    lectura = csv.reader(mificheroDelete, delimiter=',',quotechar='"')
    registro_buscado=[]
    for registros in lectura:
        if condicion == True:
            if registros[0] == str(id):
            #aqui encuentro el id buscado en mi registro
                registro_buscado.append(registros)
        else:
            if registros[0] != str(id):
                #guardamos todos menos el registro con el id para borrar
                registro_buscado.append(registros)
    mificheroDelete.close()
    return registro_buscado

def delete_by(registro_buscado):
    fichero_save = open(MOVIMIENTOS_FILE,'w', newline='')
    csvWriter = csv.writer(fichero_save, delimiter=',',quotechar='"')
    for datos in registro_buscado:
        csvWriter.writerow(datos)
    fichero_save.close()


def insert(requestForm):
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
    lectura.writerow([new_id,requestForm['fecha'],requestForm['concepto'],requestForm['monto']])
    mifichero.close()