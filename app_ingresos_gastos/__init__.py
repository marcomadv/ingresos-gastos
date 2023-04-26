from flask import Flask

app = Flask(__name__)

from app_ingresos_gastos.routes import *

#inicializar el servidor de flask
#en mac: export FLASK_APP=main.py <-- nombre del archivo en este caso main.py
#en windows: set FLASK_APP=main.py

#Comando para ejecutar el servidor en modo debug, para realizar cambios en tiempo real 
#flask --app main --debug run