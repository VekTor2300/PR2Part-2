{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "aef465af",
   "metadata": {},
   "outputs": [],
   "source": [
    "import os\n",
    "import math\n",
    "def matrix(y,x,a,b)\n",
    "        res1 = a;\n",
    "        for i in range(x)\n",
    "            for v in range (y)\n",
    "                print (str(res1),  , end='')\n",
    "                res1 = res1 + b\n",
    "            print (n)\n",
    "def kalc(a,b,c)\n",
    "    if c == '1'\n",
    "            res = ab\n",
    "            return print('Ответ ' + str(res))\n",
    "    elif c ==  '2'\n",
    "        res = ab\n",
    "        return print('Ответ ' + str(res))\n",
    "    elif c ==  '3'\n",
    "        res = a+b\n",
    "        return print('Ответ ' + str(res))\n",
    "    elif c ==  '4'\n",
    "        res = a-b\n",
    "        return print('Ответ ' + str(res))\n",
    "    elif c ==  '5'\n",
    "        res = a%b\n",
    "        return print('Ответ ' + str(res))\n",
    "    elif c ==  '6'\n",
    "        res = ab\n",
    "        return print('Ответ ' + str(res))\n",
    "    elif c == '7'\n",
    "        res = math.sin(a)\n",
    "        return print('Ответ ' + str(res))\n",
    "    elif c == '8'\n",
    "        res = math.cos(a)\n",
    "        return print('Ответ ' + str(res))\n",
    "    elif c == '9'\n",
    "        res = math.sqrt(a)\n",
    "        return print('Ответ ' + str(res))\n",
    "    elif c == '10'\n",
    "        res = math.tan(a)\n",
    "        return print('Ответ ' + str(res))\n",
    "    else\n",
    "        return print('Ошибка!!!')\n",
    "\n",
    "\n",
    "def plochad(a,b,c)\n",
    "    res = 2(ab + ac + bc)\n",
    "    return print(str(res))\n",
    "\n",
    "def perimetr(a,b,c)\n",
    "    res = 4(a+b+c)\n",
    "    return print(str(res))\n",
    "clear = lambda os.system('cls')\n",
    "\n",
    "\n",
    "vibor = input('выберите номер задания ' )\n",
    "\n",
    "if vibor == '1'\n",
    "    i = 0\n",
    "    while i != 1\n",
    "        try\n",
    "            clear()\n",
    "            k = input(' 1) площадь параллепипеда n 2) периметр параллепипеда n 3) калькулятор n Выберити действие ' )\n",
    "            \n",
    "            if k == '3'\n",
    "                \n",
    "                while i != 1\n",
    "                    c = input(' 1) умножение n 2) деление n 3) сложение n 4) вычитание n 5) нахождение остатка n 6) возведение в степень n 7) Sin n 8) Cos n 9) Корень n 10) Tan n Выберити действие ' )\n",
    "                    if c == '7' or c == '8' or c == '9' or c == '10'\n",
    "                        a = input('Введите число ')\n",
    "                        b = 0\n",
    "                    else\n",
    "                        a = input('Введите первое число ')\n",
    "                        b = input('Введите второе число ')\n",
    "                    res = kalc(int(a),int(b),c)\t\n",
    "                    i = input('Хотите продолжить(0 - нет) ')\n",
    "                    clear()\n",
    "                    if i == '0'\n",
    "                        break\n",
    "            elif k == '2'\n",
    "                while i != 1\n",
    "                    a = input('Введите первое число ')\n",
    "                    b = input('Введите второе число ')\n",
    "                    c = input('Введите второе число ')\n",
    "                    res = perimetr(int(a),int(b),int(c))\n",
    "                    i = input('Хотите продолжить(0 - нет) ')\n",
    "                    clear()\n",
    "                    if i == '0'\n",
    "                        break\n",
    "            elif k == '1'\n",
    "                while i != 1\n",
    "                    a = input('Введите первое число ')\n",
    "                    b = input('Введите второе число ')\n",
    "                    c = input('Введите второе число ')\n",
    "                    res = plochad(int(a),int(b),int(c))\n",
    "                    i = input('Хотите продолжить(0 - нет) ')\n",
    "                    clear()\n",
    "                    if i == '0'\n",
    "                        break\n",
    "            \n",
    "            else\n",
    "                print('Не правильный ввод')\n",
    "                clear()\n",
    "                \n",
    "            \n",
    "        except ValueError\n",
    "             print('Не правильный ввод')\n",
    "        \n",
    "        clear()\n",
    "        i = input('Хотите выйти из прграммы(0 - да) ')\n",
    "        if i == '0'\n",
    "            break\n",
    "elif vibor == '2'\n",
    "    s = input('Введите строку ')\n",
    "    syms1 = len(s) - s.count(' ')\n",
    "    syms2 = len(s) - syms1\n",
    "\n",
    "    syms11 = len(s) - s.count(',')\n",
    "    syms22 = len(s) - syms11\n",
    "\n",
    "    print('Символы ' + str(syms1))\n",
    "    print('Пробелы ' + str(syms2))\n",
    "    print('Запятные ' + str(syms22))\n",
    "elif vibor == '3'\n",
    "    y = input(Введите кол-во столбцов)\n",
    "    x = input(Введите кол-во строк)\n",
    "    a = input(Введите начальное число матрицы)\n",
    "    b = input(Введите шаг матрицы )\n",
    "    try\n",
    "        matrix(int(y),int(x),int(a),int(b))\n",
    "    except ValueError\n",
    "         print('Не правильный ввод')\n",
    "else\n",
    "    print('неверный выбор')\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
