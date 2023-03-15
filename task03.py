# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

import os
os.system('cls')

number = int(input('Введите число N: '))

for i in range(number):
    if 2**(i) <= number:
        print(i,end=' ')
