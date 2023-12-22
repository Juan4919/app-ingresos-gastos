from app_ingresos_gastos import app
from flask import render_template,request,redirect
import csv
from datetime import date

@app.route("/")#get
def index():
    datos =[]
    #llamada al archivo csv
    fichero = open('data/movimientos.csv','r')
    #accediendo a cada registro de archivo y darle formato
    csvReader = csv.reader(fichero,delimiter=",",quotechar='"')
    for items in csvReader:
        datos.append(items)
    fichero.close()

    return render_template("index.html",data = datos,titulo="Lista")

@app.route("/new",methods=["GET","POST"])
def new():
    if request.method== "POST":
        
        comprobar_error = validarFormulario(request.form)

        if comprobar_error:
            return render_template("new.html",titulo="Nuevo",tipoAccion="Registro",tipoBoton="Guardar",error = comprobar_error,dataForm=request.form)
        
        else:
            ######################Generar el nuevo id para registro################
            lista_id = []
            last_id = ""
            new_id = 0
            ficheroId = open('data/last_id.csv','r')
            #accediendo a cada registro de archivo y darle formato
            csvReaderId = csv.reader(ficheroId,delimiter=",",quotechar='"')
            for items in csvReaderId:
                lista_id.append(items[0])
            ficheroId.close()

            last_id = lista_id[len(lista_id)-1] #el ultimo valor del id    
            new_id = int(last_id)+1
            ######################Guardar el id generado en last_id###############
            fichero_new_id=open('data/last_id.csv','w')
            fichero_new_id.write(str(new_id))
            fichero_new_id.close()

            ########################################################################
            #acceder al archivo y configurar para la carga de nuevo registro
            mifichero = open('data/movimientos.csv','a',newline='')
            #llamar al metodo writer de escritura y configuramos formato
            lectura = csv.writer(mifichero,delimiter=',', quotechar='"')
            #registramos los datos recibidos en el archivo csv
            lectura.writerow([ new_id,request.form['fecha'],request.form['concepto'],request.form['monto'] ])
            mifichero.close()

            return redirect("/")
        
    else:#si es GET
        return render_template("new.html",titulo="Nuevo",tipoAccion="Registro",tipoBoton="Guardar",dataForm={} )

@app.route("/delete/<int:id>")
def delete(id):
    #-Consultar en data/movimientos csv y recuperar el registro con el id de la petición
    #-devolver al formulario delete.html una previsualización para luego borrarlo definitivamente con un boton

    miFicheroDelete= open('data/movimientos.csv','r')
    lecturaDelete= csv.reader(miFicheroDelete,delimiter=',',quotechar='"')
    registro_buscado=[]
    for item in lecturaDelete:
        if item[0] == str(id):
            #encuentro el id buscado de mi registro
            registro_buscado.append(item)

    
    return render_template("delete.html",titulo="Borrar",data = registro_buscado)

@app.route("/update/<int:id>")
def update(id):
    return f"El registro a editar es el de id:{id}"
    #return render_template("update.html",titulo="Actualizar",tipoAccion="Actualización",tipoBoton="Editar",dataForm={})






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