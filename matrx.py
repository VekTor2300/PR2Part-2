import os
import math
def matrix(y,x,a,b):
		res1 = a;
		for i in range(x):
			for v in range (y):
				print (str(res1), " ", end='')
				res1 = res1 + b
			print ("\n")
vibor = input('1 - Матрица ' )
if vibor == '1':
	y = input("Введите кол-во столбцов:")
	x = input("Введите кол-во строк:")
	a = input("Введите начальное число матрицы:")
	b = input("Введите шаг матрицы: ")
	try:
		matrix(int(y),int(x),int(a),int(b))
	except ValueError:
		 print('Не правильный ввод')
else:
	print('неверный выбор')
