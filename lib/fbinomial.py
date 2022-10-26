from math import factorial
from os import system
from lib.module.config import tokens, op, asciiText
from colorama import Fore, Style


system(op.cls())

	# nCx * (P**(x)) * (q**(n-x))

	# n = número de muestras

	# x >= 0 and x < n, número entre 0 y n

	# P = número de enfermos, entre 0 y 1 = float

	# nC = ((factorial(n)) / (factorial(n-x)) * (factorial(x))) * (P**(x)) * (q**(n-x))

def solve(n:int, P:float, x:int, opL:str):

	y = x

	if (x >= 0) and (x <= n) and (y >= 0) and (y<=n):

		if (P >= 0) and (P <= 1):

			q = 1 - P

			if opL == "=": 

				nCx = factorial(n) / (factorial(n-x) * factorial(x))

				solution = nCx * (P**(x)) * (q**(n-x))

				solution = round(solution, 5)

				print(f'La probabilidad de que al tomar al azar {n} individuos, {x} de ellos esten enfermos es {solution}')

			elif opL == ">=": #Mayor igual

				nCx = factorial(n) / (factorial(n-x) * factorial(x))

				solution = nCx * (P**(x)) * (q**(n-x))

				solution = round(solution, 5)

				print(f'La probabilidad de que al tomar al azar {n} individuos, {x} de ellos esten enfermos es {solution}')


				s1 = solution
					
				while(y >= x and y <= n and y >=0): #or (y == x and y <= n and y >= 0):

					y= y+1

					if (y > n): return

					nCx = factorial(n) / (factorial(n-y) * factorial(y))

					solution = nCx * (P**(y)) * (q**(n-y))

					solution = round(solution, 5)

					print(f'La probabilidad de que al tomar al azar {n} individuos, {y} de ellos esten enfermos es {solution}')

					s1 = s1 + solution

					print(f'El total es {s1}')

			elif opL == "<=": # Menor igual

				nCx = factorial(n) / (factorial(n-x) * factorial(x))

				solution = nCx * (P**(x)) * (q**(n-x))

				solution = round(solution, 5)

				print(f'La probabilidad de que al tomar al azar {n} individuos, {x} de ellos esten enfermos es {solution}')

				s1 = solution
					
				while(y <= x and y <= n and y >=0): #or (y == x and y <= n and y >= 0):

					y= y-1

					if (y < 0): return

					nCx = factorial(n) / (factorial(n-y) * factorial(y))

					solution = nCx * (P**(y)) * (q**(n-y))

					solution = round(solution, 5)

					print(f'La probabilidad de que al tomar al azar {n} individuos, {y} de ellos esten enfermos es {solution}')

					s1 = s1 + solution

					print(f'El total es {s1}')
		else: return print('Error')
	else: return print('Error')

def load() -> None:
	asciiText('./media/text/fbinomial.txt', Fore.GREEN, Style.BRIGHT, Style.RESET_ALL, '\n')

	n = int(input('Ingrese el número de muestras: '))
	P = float(input('Ingrese la probabilidad de éxito: '))
	x = int(input('Ingrese el valor que asume la variable x: '))
	opL = str(input('Ingrese el operador lógico a usar: '))

	opt = 1
	while not (opt != 1):
		solve(n, P, x, opL)
		opt = int(input('\n0 para volver al menu principal\n1 para salir\n[?]: '))
		print('\n')
		if opt == 1:
			exit()
		elif opt == 0:
			break
		else: load()
load()
    