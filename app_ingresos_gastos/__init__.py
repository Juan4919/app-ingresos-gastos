from flask import Flask

app = Flask(__name__)

from app_ingresos_gastos.routes import *

"""
 -iniciar el servidor de flask
 -en mac: 
  export FLASK_APP=main.py
 -en windows:
  set FLASK_APP=main.py
"""  

#flask --app main --debug run