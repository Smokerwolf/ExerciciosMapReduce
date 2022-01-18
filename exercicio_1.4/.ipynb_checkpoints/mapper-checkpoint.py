#!/usr/bin/python3

#Modifica o exercicio anterior para que o resultado da execución sexa o máximo absoluto de todas as vendas rexistradas.

import sys

for line in sys.stdin:
    
    data = line.strip().split("\t")
    
    if len(data) == 6:
        date, time, store, item, cost, payment = data
        print(f'all\t{cost}')
