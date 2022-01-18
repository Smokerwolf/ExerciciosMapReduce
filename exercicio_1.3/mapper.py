#!/usr/bin/python3

#Redefine o mapper e o reducer de xeito que se obteña a venda máis alta para cada tipo de pago das rexistradas en todo o ficheiro.

import sys

for line in sys.stdin:
    
    data = line.strip().split("\t")
    
    if len(data) == 6:
        date, time, store, item, cost, payment = data
        print(f'{payment}\t{cost}')
