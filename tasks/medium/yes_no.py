"""
Напишите функцию yes_or_no, которая принимает список из целых чисел,
проходит по нему и выводит Yes, если число уже встречалось и No, если нет
"""


def yes_or_no(list_1):
    for i, elem in enumerate(list_1):
        if elem in list_1[:i]:
            print('Yes')
        else:
            print('No')


list1 = [1, 2, 3, 1, 1, 2, 4]
yes_or_no(list1)
