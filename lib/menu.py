from os import system
from lib.module.switch import switch
from lib.module.asciiConsole import asciiText
from colorama import Fore, Style, init
from lib.module.osIdentifier import op
import time

def main():
    init(autoreset=True)
    system(op.cls())
    # https://www.ascii-art-generator.org/es.html
    
    asciiText('./media/text/menu.txt', Fore.RED, Style.BRIGHT, Style.RESET_ALL)
    print("""
    [0] Salir                      [5] Descargar canciones   
    [1] Torre de hanoi             [6] Búsqueda en Google
    [2] Función binomial           [7] Búsqueda en DuckDuckGo
    [3] Generador de códigos QR    [8] Búsqueda en Youtube
    [4] Búsqueda de libros         [9] Acortador de URL
    """)
    try:
        opt = 0
        opt = int(input('[?] Que quieres hacer? '))

        with switch(opt) as s:

            if s.case(0, True):
                system(op.cls())
                exit()

            if s.case(1, True):
                opt = 0
                import lib.hanoi
                
            if s.case(2, True):
                opt = 0
                import lib.fbinomial

            if s.case(3, True):
                opt = 0
                import lib.qrcode

            if s.case(4, True):
                opt = 0
                import lib.apify.bookScraper

            if s.case(5, True):
                opt = 0
                import lib.mp3Download

            if s.case(6, True):
                opt = 0
                import lib.gSearch

            if s.case(7, True):
                opt = 0
                import lib.apify.ddgScraper

            if s.case(8, True):
                opt = 0
                import lib.apify.ytScraper
            
            if s.case(9, True):
                opt = 0
                import lib.urlShort

            if s.default():
                opt = 0
                print('Esa opción no esta disponible, escoge otra')
                time.sleep(5)
                main()

    except ValueError:
        print('Valor inválido')
        main()

    except KeyboardInterrupt:
        main()

action = 1

while (action == 1):
    try:
        main()
        system(op.cls())
        print(f'{Style.BRIGHT}Menú de salida{Style.RESET_ALL}')
        action = int(input('\n0 para salir\n1 para el menú principal\n[?]: '))
        if action != 0:
            main()
        exit()

    except ValueError:
        print('Valor inválido')
        main()

    except KeyboardInterrupt:
        main()