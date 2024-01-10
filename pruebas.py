# lectura de archivos
"""
with open('data/movimientos.csv','r') as resultado:
    leer = resultado.read()
    print(type(leer))
"""
#otro ejemplo de lectura de archivos csv
"""
resultado = open('data/movimientos.csv','r')
lectura = resultado.readlines()
print(lectura)   
"""
"""
import csv

midato= []
mifichero = open('data/movimientos.csv','r')
lectura = csv.reader(mifichero,delimiter=",",quotechar='"')
for items in lectura:
    #print(type(items))
    midato.append(items)

print("mi lista:",midato[0][1])    
"""
#ejemplo para registrar datos en csv
"""
import csv

mifichero = open('data/movimientos.csv','a',newline='')
lectura = csv.writer(mifichero,delimiter=',', quotechar='"')
lectura.writerow(['24/04/2024','roscon de reyes','-40'])

mifichero.close()
"""
"""
from datetime import date

print(type(str(date.today())))
print(date.today())
"""
"""
comprobar_error=[1,2,3]@
if len(comprobar_error) > 0:
    print("si tiene valores")
else:
    print("no tiene valores")    

"""

#lista=[22,11,44,11,66,878,2323,343,67676,888,33]

#print(lista[ len(lista)-1 ] )#obtener el ultimo valor de una lista

lista_csv = [5,"2024-04-01","kjfdkjdfk",12121] 
lista_para_mostrar=[ ]

#lista_para_mostrar.append(lista_csv)
lista_para_mostrar = lista_csv
print(lista_para_mostrar[1])