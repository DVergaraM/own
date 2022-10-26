from os import system
from lib.module.config import tokens
from lib.module.builtIn import op, asciiText
from colorama import Fore, Style
from pyshorteners import Shortener

system(op.cls())

def generate(url:str):
    tiny = Shortener()
    short = tiny.tinyurl.short(url)
    print(f'El enlace acortado es: {short}')

def main():
    asciiText('./media/text/urlShort.txt', Fore.CYAN, Style.BRIGHT, Style.RESET_ALL, '\n')

    link = str(input('Ingrese un enlace: '))
    opt = 1
    while not (opt != 1):
        generate(link)
        opt = int(input('\n0 para volver al menu principal\n1 para salir\n[?]: '))
        print('\n')
        if opt == 1:
            exit()
        elif opt == 0:
            break
        else: main()
main()