# Задача: предложить улучшения кода для уже решённых задач:

# # 1.Задайте список из нескольких чисел. Напишите программу,
# # которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# # *Пример:*
# # - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

# list = [2, 3, 5, 9, 3]
# print(sum(list[1::2]))

# Другой вариант
spisok = [2, 3, 5, 9, 3]

res =[spisok[x] for x in range(len(spisok)-1) if x % 2 != 0]

print(f'сумма элементов списка, стоящих на нечётной позиции составляет {sum(list(res))}')