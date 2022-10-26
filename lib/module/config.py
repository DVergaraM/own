"""
To get an Apify API Token, go to https://console.apify.com/account?tab=integrations
"""
class tokens:
    apifyKey = "apify_api_LjIF2BM8gjfSuzsX5gu4SVDhh59soB3wYj2U"








from platform import system

class op:
    def cls():
        clear = ''

        if system() != 'Windows':
            clear = 'clear'
        else:
            clear = 'cls'

        return clear

from colorama import Fore, Style

def asciiText(path:str='./media/text/menu.txt', color:str=Fore.RED, style:str=Style.BRIGHT, rStyle:str=Style.RESET_ALL, jump:str=''):
	try:
		file = open(path, encoding='utf-8').read()
		print(style + color + file + rStyle + jump)
	except FileNotFoundError:
		print(f'{path} no existe, cree el archivo e introduzca un texto tipo ASCII para continuar.')
		exit()