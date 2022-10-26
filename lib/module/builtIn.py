from platform import system
from colorama import Fore, Style

class op:
    def cls():
        clear = ''

        if system() != 'Windows':
            clear = 'clear'
        else:
            clear = 'cls'

        return clear


def asciiText(path:str='./media/text/menu.txt', color:str=Fore.RED, style:str=Style.BRIGHT, rStyle:str=Style.RESET_ALL, jump:str=''):
	try:
		file = open(path, encoding='utf-8').read()
		print(style + color + file + rStyle + jump)
	except FileNotFoundError:
		print(f'{path} no existe, cree el archivo e introduzca un texto tipo ASCII para continuar.')
		exit()