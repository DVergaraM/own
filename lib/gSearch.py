from googlesearch import search as gsearch
import os
from .module.config import tokens, op, asciiText
from colorama import Fore, Style


os.system(op.cls())

def s(query:str) -> str:
    e = r'C:\\Users\\verga\\OneDrive\\Escritorio\\rqaw\Documentos\Dev\\Python\\Colegio\\media\\googleResults\\' + query + '.txt'
    return e

def search(query:str, lang:str='es'):
    if lang == '': lang = 'es'
    try: 
        queryJoin = '-'.join(query.split(" "))
        file = open(s(queryJoin), 'a', encoding="UTF-8")
        for item in gsearch(query, lang=lang):
            try: 
                file.write(f"""
                {item}\n
                """)
            except UnicodeEncodeError or KeyboardInterrupt:
                break
        file.close()
        print(f'\nSe ha terminado de buscar resultados para {query}, los puede encontrar en "media/results/{queryJoin}.txt"')
    except FileExistsError or UnicodeEncodeError or KeyboardInterrupt:
        pass
    except OSError:
        exit()


def main():
    asciiText('./media/text/gSearch.txt', Fore.GREEN, Style.BRIGHT, Style.RESET_ALL, '\n')

    query = str(input('Que quiere buscar?: '))

    opt = 1
    while not (opt != 1):
        search(query)
        opt = int(input('\n0 para volver al menu principal\n1 para salir\n[?]: '))
        print('\n')
        if opt == 1:
            exit()
        elif opt == 0:
            break
        else: main()
main()