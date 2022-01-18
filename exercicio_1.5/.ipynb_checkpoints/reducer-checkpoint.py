#!/usr/bin/python3
import sys

#Redefine o mapper e o reducer de xeito que se obteña o total de vendas.

VentasTotales = 0
oldKey = None

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    thisKey, thisSale = data_mapped

    if oldKey != thisKey:
        print(oldKey, "\t", VentasTotales)
        oldKey = thisKey;
        VentasTotales = 0

    oldKey = thisKey
    VentasTotales += float(thisSale)

if oldKey != None:
    print(oldKey, "\t", VentasTotales)
