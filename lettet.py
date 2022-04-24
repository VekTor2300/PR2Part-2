s = input('Введите строку: ')
syms1 = len(s) - s.count(' ')
syms2 = len(s) - syms1

syms11 = len(s) - s.count(',')
syms22 = len(s) - syms11

print('Символы: ' + str(syms1))
print('Пробелы: ' + str(syms2))
print('Запятные: ' + str(syms22))
