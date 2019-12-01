import numpy as np
import math
import sys

## Proyecto  Final de Sistemas Operativos
## 2 de diciembre de 2019

class process(object):
    def __init__(self, nombre, size, inicio, swap):
        self.id = nombre
        self.tam = size
        self.pags = math.ceil(op1/16)
        self.i = inicio
        self.sw = swap

arrprocess = []                         # Arreglo de objetos (Lista de procesos)
op0 = 0                                 # En una instrucción 'A 82 1 0'
op1 = 0                                 # op0 = A, op1 = 82, op2 = 1, op3 = 0
op2 = 0
op3 = 0

infile = open("input.mem", "r")         # Lee el archivo "input.mem", donde se encuentran los comandos
texto = infile.readlines()              # Lee cada linea y las guarda en una lista
texto.reverse()                         # Se reversea el texto para que se haga pop a la primera instrucción

while(op0 != 'E'):
    line = texto.pop()                  # En 'line' se guarda la primera línea del archivo
    line = line.split()                 # Se separa cada palabra en un espacio de la lista
    op0 = line[0]                       # Se lee la operación que se hará

    if op0 == 'C':                      # Operación de comentarios
        line.reverse()                  # Se reversea la lista para hacer pop al primero
        line.pop()                      # Se quita la 'C' de la instrucción
        line.reverse()                  # Se vuelve a la normalidad la lista y se imprimen sus contenidos
        for n in line:
            print(n, end = ' ')
        print()

    if op0 == 'F':                                      # Finalizan las operaciones y se reinicia todo
        print()
        print('== FIN DE LOS PROCESOS ==')
        print() 
        
print('== ADIOS ==')
print()