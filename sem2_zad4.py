#Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt в одной строке одно число.
import functools
n = int(input('Введите число: '))

num_list = [i for i in range(-n,n+1)]
print(num_list)

f=open('file.txt','r')
pos=f.read()
list_pos=pos.split('\n')
positions = list(map(int,list_pos))
print(list_pos)

count = functools.reduce(lambda x,y: x*y,
                         [v for i, v in enumerate(num_list) if i in positions])
print(count)
