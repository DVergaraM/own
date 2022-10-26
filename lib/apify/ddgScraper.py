from lib.apify.keys import key
from apify_client import ApifyClient
from os import system
from lib.module.asciiConsole import asciiText
from colorama import Fore, Style
from lib.module.osIdentifier import op

system(op.cls())
def s(query:str) -> str:
    e = r'C:\\Users\\verga\\OneDrive\\Escritorio\\rqaw\Documentos\Dev\\Python\\Colegio\\media\\duckDGoResults\\' + query + '.txt'
    return e

def search(query:str):
    queryJoin = '-'.join(query.split(" "))
    file = open(s(queryJoin), "a", encoding="UTF-8")    
    client = ApifyClient(key.key)

    scraper = client.actor("cyberfly/duckduckgo").call(run_input = {
     "SearchTerm": query 
    })

    
    for item in client.dataset(scraper["defaultDatasetId"]).iterate_items():

        try: 
            file.write(f"""
            Titulo: {item['title']}
            Descripción: {item['description']}
            Enlace: {item['url']}
            \n\n\n\n
            """)
        except UnicodeEncodeError or KeyboardInterrupt:
            break
    file.close()
    print(f'\nSe ha terminado de buscar resultados para {query}, los puede encontrar en "media/duckDGoResults/{queryJoin}.txt"')
    
def main():
    asciiText('./media/text/duckDGoScraper.txt', Fore.GREEN, Style.BRIGHT, Style.RESET_ALL)

    query = str(input('Introduzca un termino o frase a buscar: '))
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