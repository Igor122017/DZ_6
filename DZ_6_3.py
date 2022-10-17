# Задача: предложить улучшения кода для уже решённых задач:
# Задайте последовательность чисел. Напишите программу, которая выведет список
# неповторяющихся элементов исходной последовательности.
# С помощью использования **лямбд, filter, map, zip, enumerate, list comprehension

# исходный код

# lst = list(map(int, input("Введите числа через пробел:\n").split()))
# print(f"Исходный список: {lst}")
# new_lst = []
# [new_lst.append(i) for i in lst if i not in new_lst]
# print(f"Список из неповторяющихся элементов: {new_lst}")

import random
range_num, num = 10, 10

number = [random.randint(0, range_num) for num in range(num)]

sort_unical = [x for x in number if number.count(x) == 1]
print(f'исходный список {number} список неповторяющихся элементов  {sort_unical}')


# Другойвариант с помощью lambda и filter

unical= lambda x: number.count(x) == 1

result_list= filter(unical,number)

print(f'исходный список {number} список неповторяющихся элементов  {list(result_list)}')