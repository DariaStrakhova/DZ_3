# Задача 18: Требуется найти в массиве A[1..n] самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число n – количество элементов в массиве. В последующих  
# строках записаны n целых чисел Ai. Последняя строка содержит число X

import random

n = int(input("Введите количество элементов в массиве "))
list = [random.randint(1, 10) for i in range(n)]
print(list)
x = int(input("Введите число "))
index_element = 0
min_element = abs(x - list[0])
for i in range(1, n):
    buffer_element = abs(x -list[i])
    if buffer_element < min_element:
        min_element = buffer_element
        index_element = i

print(f"Самый близкий по величине элемент к числу {x}: {list[index_element]}")