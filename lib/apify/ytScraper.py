from apify_client import ApifyClient
from os import system
from lib.module.config import tokens
from lib.module.builtIn import op, asciiText
from colorama import Fore, Style

import time

system(op.cls())
def s(query:str) -> str:
    e = r'C:\\Users\\verga\\OneDrive\\Escritorio\\rqaw\Documentos\Dev\\Python\\Colegio\\media\\youtubeResults\\' + query + '.txt'
    return e

def search(query:str):
    queryJoin = '-'.join(query.split(" "))
    file = open(s(queryJoin), "a", encoding="UTF-8")    
    client = ApifyClient(tokens.apifyKey)

    scraper = client.actor("jupri/youtube-browser").call( run_input = {
    "query": query
    })
    
    for item in client.dataset(scraper["defaultDatasetId"]).iterate_items():

        try: 
            file.write(f"""
            Nombre: {item['name']}
            Enlace: {item['url']}
            Duración: {item['overview']['length']}
            Vistas: {item['viewCount']}
            Canal: {item['channel']['name']}
            Enlace del canal: {item['channel']['url']}
            Categoria: {item['category']}
            Fecha de subida: {item['uploadDate']}
            \n\n\n\n
            """)
        except UnicodeEncodeError or KeyboardInterrupt:
            break
    file.close()
    print(f'\nSe ha terminado de buscar resultados para {query}, los puede encontrar en "media/youtubeResults/{queryJoin}.txt"')
    
def main():
    asciiText('./media/text/YTScraper.txt', Fore.BLUE, Style.BRIGHT, Style.RESET_ALL)

    query = str(input('Que desea buscar?: '))
    opt = 1
    while not (opt != 1):
        import lib.module.load
        search(query)
        opt = int(input('\n0 para volver al menu principal\n1 para salir\n[?]: '))
        print('\n')
        if opt == 1:
            exit()
        elif opt == 0:
            break
        else: main()
main()