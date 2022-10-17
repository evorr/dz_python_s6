#Реализуйте алгоритм перемешивания списка.

numbers = [1,2,3,4,5,6,7,8]
print(numbers)
new_seq = [numbers[-i-1] for i in range(0,len(numbers))]
print(new_seq)