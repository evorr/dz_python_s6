#Реализуйте алгоритм перемешивания списка.

list=[1,2,3,4,5,6,7,8]
print(list)
for i in range(0,len(list)//2):
    temp=list[i]
    list[i]=list[-i-1]
    list[-i-1]=temp
print(list)