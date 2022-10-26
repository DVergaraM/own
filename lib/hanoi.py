from lib.module.switch import switch
from os import system
from lib.module.config import tokens
from lib.module.builtIn import op, asciiText

from colorama import Fore, Style
n = 0
org = ''
dest = ''
aux = ''

def solve(n:int=4, org:str="A", dest:str="B", aux:str="C"):
    try:
        if org == '': org = 'A'
        if dest == '': dest = 'B'
        if aux == '': aux = 'C'
        if n == None: n = 4

        with switch(n) as s:

            if s.case(1):

                print(f'Mueva el disco {n} desde la torre {org} hasta la torre {dest}')

            if s.default():

                solve(n-1, org, aux, dest)

                print(f'Mueva el disco {n} desde la torre {org} hasta la torre {dest}')

                solve(n-1, aux, dest, org)
    except RecursionError:
        print('Error de recursión')
        exit()
def min(n:int):
	movements = (2**n) - 1
	print(f'El total de movimientos fue {movements}')

def main():
    system(op.cls())
    opt = 1
    asciiText('./media/text/hanoi.txt', Fore.BLUE, Style.BRIGHT, Style.RESET_ALL, '\n')

    n = int(input('Ingrese la cantidad de discos: '))
    org = str(input('Ingrese la columna de inicio: '))
    dest = str(input('Ingrese la columna de destino: '))
    aux = str(input('Ingrese la columna auxiliar: '))
    print('\n')
    while not (opt != 1):
        solve(n, org, dest, aux)
        min(n)
    
        opt = int(input('\n0 para volver al menu principal\n1 para salir\n[?]: '))
        print('\n')
        if opt == 1:
            exit()
        elif opt == 0:
            break
        else: main()
main()
