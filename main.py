import numpy as np
import math
import sys

## Proyecto  Final de Sistemas Operativos
## 2 de diciembre de 2019

class process(object):
    def __init__(self, nombre, size, inicio):
        self.id = nombre
        self.tam = size
        self.pags = math.ceil(size/16)
        self.i = inicio
        self.sw = swap
        self.pf = 0

class memoria(object):
    def __init__(self, pos, id, val, swap):
        self.pos = pos
        self.id = id
        self.val = val
        self.sw = swap

arrprocess = []                         # Arreglo de objetos (Lista de procesos)
mem = []
swap = []
for n in range(128):
    mem.append(memoria(n, 0, 0, 0))
for n in range(256):
    swap.append(memoria(n, 0, 0, 1))

#print(mem[0].pos)
#print(mem[0].id)
#print(mem[0].val)
#print(mem[0].sw)

swap = [] * 256
op0 = 0                                 # En una instrucción 'A 82 1 0'
op1 = 0                                 # op0 = A, op1 = 82, op2 = 1, op3 = 0
op2 = 0
op3 = 0
swap_in = 0
swap_out = 0

def reset():
    global arrprocess, op0, op1, op2, op3
    arrprocess = []
    op0 = 0
    op1 = 0
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

    if op0 == 'P':
        0

    if op0 == 'A':
        0

    if op0 == 'L':
        0
        
    if op0 == 'F':                                      # Finalizan las operaciones y se reinicia todo
        print()
        reset()
        print('== FIN DE LOS PROCESOS ==')
        print() 
        
print('== ADIOS ==')
print()