from app_ingresos_gastos import app,MOVIMIENTOS_FILE,LAST_ID_FILE
from flask import render_template,request,redirect
import csv
from datetime import date
from app_ingresos_gastos.models import *

@app.route("/")#get
def index():
    datos = select_all()
    return render_template("index.html",data = datos,titulo="Lista")

@app.route("/new",methods=["GET","POST"])
def new():
    if request.method== "POST":
        
        comprobar_error = validarFormulario(request.form)

        if comprobar_error:
            return render_template("new.html",titulo="Nuevo",tipoAccion="Registro",tipoBoton="Guardar",error = comprobar_error,dataForm=request.form)
        
        else:

            insert(request.form)

            return redirect("/")
        
    else:#si es GET
        return render_template("new.html",titulo="Nuevo",tipoAccion="Registro",tipoBoton="Guardar",dataForm={} ,urlForm="/new")

@app.route("/delete/<int:id>",methods=["GET","POST"])
def delete(id):
    if request.method == "GET":

        registro_buscado = select_by(id,"==")
        
        return render_template("delete.html",titulo="Borrar",data = registro_buscado)
    else:#post

        registros=select_by(id,"!=")

        delete_by(id,registros=registros)

        return redirect("/")


@app.route("/update/<int:id>",methods=["GET","POST"])
def update(id):
    if request.method == "POST":
       
       comprobar_error = validarFormulario(request.form)
       if comprobar_error:
             return render_template("update.html",titulo="Actualizar",tipoAccion="Actualización",tipoBoton="Editar",error = comprobar_error,dataForm=request.form,urlForm=f"/update/{id}")    
      
       formulario=request.form
       registros= select_all()
       update_item(id,registros,formulario)

       return redirect("/")
    else:
      
        registro_buscado= select_by(id,"dic")
        
        return render_template("update.html",titulo="Actualizar",tipoAccion="Actualización",tipoBoton="Editar",dataForm=registro_buscado,urlForm=f"/update/{id}")




"""
-Que la fecha ingresada no sea mayor que la actual
-que el concepto no vaya vació
-que el monto sea distinto de 0 y de vacio
"""
def validarFormulario(datosFormulario):
    errores =[]#crear lista para guardar errores
    hoy = str(date.today())#esto quita la fecha de hoy
    if datosFormulario['fecha'] > hoy:
        errores.append("La fecha no puede ser mayor a la actual")
    if datosFormulario['concepto'] == "":
        errores.append("El concepto no puede ir vacio")
    if datosFormulario['monto'] =="" or float(datosFormulario['monto']) == 0.0: 
        errores.append("El monto debe ser distinto de 0 y de vacio")


    return errores            