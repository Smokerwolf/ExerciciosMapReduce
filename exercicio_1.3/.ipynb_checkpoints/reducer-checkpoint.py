#!/usr/bin/python3

import sys

VendaMaior = 0
oldKey = None

#Redefine o mapper e o reducer de xeito que se obteña a venda máis alta para cada tipo de pago das rexistradas en todo o ficheiro.

for line in sys.stdin:
    
    data_mapped = line.strip().split("\t")
    
    if len(data_mapped) != 2:
        continue

    thisKey, thisSale = data_mapped

    if oldKey != thisKey:
        print(oldKey, "\t", VendaMaior)
        VendaMaior = 0

    oldKey = thisKey
    
    if (thisSale >= VendaMaior):
        VendaMaior = float(thisSale)

if oldKey != None:
    print(oldKey, "\t", VendaMaior)
