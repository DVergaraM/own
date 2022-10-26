from pyqrcode import create
import png
from PIL import Image
from os import system
from lib.module.asciiConsole import asciiText
from colorama import Fore, Style
from lib.module.osIdentifier import op

system(op.cls())

def generate(url:str, fileName:str):
    qrCode = create(url)
    fileNameJoin = '-'.join(fileName.split(" "))
    qrCode.png(f'media/qrCode/{fileNameJoin}.png', scale=5)
    Image.open(f'media/qrCode/{fileNameJoin}.png')

def main():
    asciiText('./media/text/qrcode.txt', Fore.CYAN, Style.BRIGHT, Style.RESET_ALL, '\n')

    link = str(input('Ingrese un enlace: '))
    fileName = str(input('Ingrese un nombre de guardado: '))
    opt = 1
    while not (opt != 1):
        generate(link, fileName)
        opt = int(input('\n0 para volver al menu principal\n1 para salir\n[?]: '))
        print('\n')
        if opt == 1:
            exit()
        elif opt == 0:
            break
        else: main()
main()