#!/usr/bin/python3

#Importaciones--------
import sys
#---------------------

#Variables------------
#Podría usar un diccionario, cuya clave sea la categoria
#el método de pago y el valor sea pues el total de ventas
diccionario = {}
#---------------------

for line in sys.stdin:
    data = line.strip().split("\t")
    
    #Si encuentra una linea que no tenga 6 elementos, la ignora
    if len(data) != 6:
    	continue
    

    date, time, store, item, cost, payment = data
    if payment in diccionario:
        diccionario[payment] += float(cost)
    else:
        diccionario.update({ payment : float(cost) })
    
for key,value in diccionario.items():
    print("Método de pago: {} | Cantidad: {}".format(key,format(value, ".2f")))
#print(diccionario)
