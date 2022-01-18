#!/usr/bin/python3
import sys

#Modifica o exercicio anterior para que o resultado da execución sexa o máximo absoluto de todas as vendas rexistradas.

VentasMaximoAbsoluto = 0
oldKey = None

for line in sys.stdin:
    
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        continue

    thisKey, thisSale = data_mapped

    if oldKey and oldKey != thisKey:
        print(oldKey, "\t", VentasMaximoAbsoluto)
        VentasMaximoAbsoluto = 0

    oldKey = thisKey
    if (thisSale >= VentasMaximoAbsoluto):
        VentasMaximoAbsoluto = float(thisSale)

if oldKey != None:
    print(oldKey, "\t", VentasMaximoAbsoluto)
