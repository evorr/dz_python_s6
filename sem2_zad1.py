#Напишите программу, которая принимает на вход вещественное число
# и показывает сумму его цифр.
#Пример:
#- 6782 -> 23
#- 0,56 -> 11
import functools
num = input('Введите вещественное число: ')

def chek(n):
    if n not in (',','.'):
        return n
count = functools.reduce(lambda x,y: x+y,map(int,(filter(chek, num))))

print(f'{num} -> {count}')
