# Задайте список из нескольких чисел. Напишите программу,
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# *Пример:*
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
import functools

num_list=[4,3,4,8,1,9,2]

odd_nums = [v for i,v in enumerate(num_list) if i%2!=0]
sum_elem = functools.reduce(lambda x,y: x+y, odd_nums)

print(f'{num_list} -> на нечётных позициях элементы {odd_nums}, ответ: {sum_elem}')