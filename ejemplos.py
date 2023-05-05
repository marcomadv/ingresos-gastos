# lectura de archivos
'''
with open('data/movimientos.csv',"r") as resultado:
    leer = resultado.read()
'''
#otro ejemplo (lo guarda como una lista)
'''
resultado = open('data/movimientos.csv','r')
lectura = resultado.readlines()
print(lectura)
'''

import csv
'''
midato = []
mifichero = open('data/movimientos.csv','r')
lectura = csv.reader(mifichero)

for items in lectura:
    print(items)
    midato.append(items)

print("mi lista: ",midato) #lista de listas
'''
'''
mifichero = open('data/movimientos.csv','a')
lectura = csv.writer(mifichero,delimiter=',',quotechar='"')
lectura.writerow(['25/04/2023','compra de zapatillas','-100'])
mifichero.close()
'''

lista_id = ['1','2,','3','4','20','300']

last_id= lista_id[len(lista_id)-1]

print(last_id)