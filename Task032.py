"""
Определить индексы элементов массива (списка), 
значения которых принадлежат заданному диапазону 
(т.е. не меньше заданного минимума и не больше заданного максимума)
"""

import random

arr = [random.randint(0, 20) for i in range(10)]
print(arr)

min_number = int(input("Введите минимальный диапазон : "))
max_number = int(input("Введите максимальный диапазон : "))

print(*[i for i in range(len(arr)) if min_number <= arr[i] <= max_number])