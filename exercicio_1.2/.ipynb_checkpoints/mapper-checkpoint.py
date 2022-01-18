#!/usr/bin/python3

#Redefine o mapper e o reducer de xeito que devolvan un ficheiro co total de vendas por categoría.

import sys

for line in sys.stdin:
    
    data = line.strip().split("\t")
    
    if len(data) == 6:
        date, time, store, item, cost, payment = data
        print(f'{item}\t{cost}')
