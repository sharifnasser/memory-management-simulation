import numpy as np
import math
import sys

## Proyecto  Final de Sistemas Operativos
## 2 de diciembre de 2019

class process(object):
    def __init__(self, nombre, size, inicio, final, swap):
        self.id = nombre
        self.tam = size
        self.pags = math.ceil(op1/16)
        self.i = inicio
        self.f = final
        self.sw = swap

arrprocess = []                         # Arreglo de objetos (Lista de procesos)
mem = [None] * 128                      # Memoria principal: 2048 bits / 128 páginas
swap = [None] * 256                     # Memoria principal: 4096 bits / 256 páginas
mem_n = 0                               # Contador de posición en memoria
swap_n = 0                              # Contador de posición en swap
op0 = 0                                 # En una instrucción 'A 82 1 0'
op1 = 0                                 # op0 = A, op1 = 82, op2 = 1, op3 = 0
op2 = 0
op3 = 0
minmem = 0                              # Variable donde se almacena la pos. inicial de un proceso si esta en memoria
maxmem = 0                              # Variable donde se almacena la pos. final de un proceso si esta en memoria
minswap = 0                             # Variable donde se almacena la pos. inicial de un proceso si esta en swap
maxswap = 0                             # Variable donde se almacena la pos. final de un proceso si esta en swap
tamtotal = 0                            # Tamaño total de los procesos, usado para no dejar que se meta un proceso si la mem. principal y la swap estan llenas

def reset():
    global arrprocess, mem, swap, mem_n, swap_n, op0, op1, op2, op3, minmem, maxmem, minswap, maxswap, tamtotal
    arrprocess = []                         # Arreglo de objetos (Lista de procesos)
    mem = [None] * 128                      # Memoria principal: 2048 bits / 128 páginas
    swap = [None] * 256                     # Memoria principal: 4096 bits / 256 páginas
    mem_n = 0                               # Contador de posición en memoria
    swap_n = 0                              # Contador de posición en swap
    op0 = 0                                 # En una instrucción 'A 82 1 0'
    op1 = 0                                 # op0 = A, op1 = 82, op2 = 1, op3 = 0
    op2 = 0
    op3 = 0
    minmem = 0                              # Variable donde se almacena la pos. inicial de un proceso si esta en memoria
    maxmem = 0                              # Variable donde se almacena la pos. final de un proceso si esta en memoria
    minswap = 0                             # Variable donde se almacena la pos. inicial de un proceso si esta en swap
    maxswap = 0                             # Variable donde se almacena la pos. final de un proceso si esta en swap
    tamtotal = 0                            # Tamaño total de los procesos, usado para no dejar que se meta un proceso si la mem. principal y la swap estan llenas

reset()
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
        
    if op0 == 'P':                      # Operación de asignación de memoria
        op1 = int(line[1])
        op2 = line[2]
        tamtotal += op1
        
        if op1 <= 2048 or tamtotal <= 6144:
            print('Asignar', op1, 'bytes al proceso', op2)
            arrprocess.append(process(op2, op1, 0, 0, 0))
            pag = math.ceil(op1/16)
            temp = pag
            while(temp > 0):
                if mem[mem_n] == None:
                    if temp == pag:
                        minmem = mem_n
                    if temp == 1:
                        maxmem = mem_n
                        for obj in arrprocess:
                            if obj.id == op2:
                                obj.i = minmem
                                obj.f = maxmem
                    mem[mem_n] = op2
                    mem_n += 1
                    temp -= 1
                    if mem_n == 128:
                        mem_n = 0
                else:
                    for obj in arrprocess:
                        tempmem = mem_n
                        if mem[tempmem] == obj.id:
                            obj.sw = 1
                            for n in range(obj.pags):
                                if n == 0:
                                    minswap = swap_n
                                if n == (obj.pags-1):
                                    maxswap = swap_n
                                    obj.i = minswap
                                    obj.f = maxswap
                                swap[swap_n] = mem[tempmem]
                                mem[tempmem] = None
                                tempmem += 1
                                swap_n += 1
                                if tempmem == 128:
                                    tempmem = 0
                                if swap_n == 256:
                                    swap_n = 0
                            print('Proceso', obj.id, 'swappeado a [', obj.i, '-', obj.f, '] de la memorial swap. Tam =', obj.pags)
            if minmem == maxmem:
                print('Proceso', op2, 'asignado a [', obj.i, ']de la memoria principal. Tam =', pag)
            else:
                print('Proceso', op2, 'asignado a [', obj.i, '-', obj.f, '] de la memoria principal. Tam =', pag)
        else:
            print('-ERROR- EL PROCESO ES MUY GRANDE PARA CABER EN MEMORIA O MEMORIA LLENA')
        if tamtotal > 6144:
            tamtotal -= op1
        print(mem)
        print(swap)

    if op0 == 'A':                                      # Operación para accesar a memoria y direcciones
        op1 = int(line[1])
        op2 = line[2]
        op3 = int(line[3])
        for obj in arrprocess:
            if op2 == obj.id:
                print('Proceso:', obj.id, end='')
                print('. Direccion virtual:', op1, end='')
                print('. Direccion real:', ((obj.i*16) + op1), end='')
                print('.')
 
    if op0 == 'L':                                      # Operación para liberar procesos
        op1 = line[1]
        for obj in arrprocess:
            if op1 == obj.id:
                for n in range(obj.pags):
                    if obj.sw == 0:
                        mem_n = obj.i
                        mem[(temp*16)+n] = None
                    elif obj.sw == 1:
                        swap_n = obj.i
                        swap[(temp*16)+n] = None
                
                arrprocess.remove(obj)
                print('Se libera el proceso', obj.id, )

    if op0 == 'F':                                      # Finalizan las operaciones y se reinicia todo
        print()
        for obj in arrprocess:
            arrprocess.remove(obj)
        reset()
        print('== FIN DE LOS PROCESOS ==')
        print() 
        
print('== ADIOS ==')
print()