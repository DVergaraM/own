from lib.module.config import tokens, op, asciiText
from apify_client import ApifyClient
from os import system
from colorama import Fore, Style

system(op.cls())
def s(book:str) -> str:
    e = r'C:\\Users\\verga\\OneDrive\\Escritorio\\rqaw\Documentos\Dev\\Python\\Colegio\\media\\books\\' + book + '.txt'
    return e

def search(book:str, type:str):
    bookJoin = '-'.join(book.split(" "))
    file = open(s(bookJoin), "a", encoding="UTF-8")    
    client = ApifyClient(tokens.apifyKey)

    scraper = client.actor("perci/z-library-book-scraper").call( run_input = {
    "search": book,
    "proxyConfig": { "useApifyProxy": False },
    })
    type = type.upper()

    
    for item in client.dataset(scraper["defaultDatasetId"]).iterate_items():

        try: 
            if item['FileType'] != type: type = 'PDF'
            file.write(f"""
            Titulo: {item['Title']}
            Autor: {item['Author']}
            Publicador: {item['Publisher']}
            Año: {item['Year']}
            Idioma: {item['Language']}
            ISBN: {item['ISBN']}
            Tipo de archivo: {type}
            Tamaño: {item['Size']}
            Puntaje de interés: {item['InterestRating']}
            Puntaje de calidad: {item['QualityRating']}
            Enlace: {item['Link']}
            \n\n\n\n
            """)
        except UnicodeEncodeError or KeyboardInterrupt:
            break
    file.close()
    print(f'\nSe ha terminado de buscar resultados para {book}, los puede encontrar en "media/books/{bookJoin}.txt"')
    
def main():
    asciiText('./media/text/bookScraper.txt', Fore.MAGENTA, Style.BRIGHT, Style.RESET_ALL)

    book = str(input('Introduzca el libro a buscar: '))
    ext = str(input('Introduzca la extensión: '))
    opt = 1
    while not (opt != 1):
        import lib.module.load
        search(book, ext)
        opt = int(input('\n0 para volver al menu principal\n1 para salir\n[?]: '))
        print('\n')
        if opt == 1:
            exit()
        elif opt == 0:
            break
        else: main()
main()