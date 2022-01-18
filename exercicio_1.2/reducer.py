#!/usr/bin/python3
import sys

TotalVendas = 0
oldKey = None

#Redefine o mapper e o reducer de xeito que devolvan un ficheiro co total de vendas por categoría.


for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    thisKey, thisSale = data_mapped

    if oldKey != thisKey:
        print(oldKey, "\t", TotalVendas)
        oldKey = thisKey;
        TotalVendas = 0

    oldKey = thisKey
    TotalVendas += float(thisSale)

if oldKey != None:
    print(oldKey, "\t", TotalVendas)
