#Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt в одной строке одно число.
n = int(input('Введите число: '))
list=[]
for i in range(-n,n+1):
    list.append(i)
print(list)
f=open('file.txt','r')
pos=f.read()
list_pos=pos.split('\n')
print(list_pos)
count=1
for i in list_pos:
    count*=list[int(i)]
print(count)
