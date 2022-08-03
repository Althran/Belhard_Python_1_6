"""
Написать функцию count_char, которая принимает строковое значение STR_VAL,
из которого создает и возвращает словарь, следующего вида:
{
    'буква': количество-вхождений-в-строку
}

например: {
    'p': 2,
    'y': 1,
    ...
}

Нельзя пользоваться collections.Counter!
"""
STR_VAL = 'python is the fastest-growing major programming language'


def count_char(string):
    data = {}
    new_string = string.replace(' ', '')
    for i in new_string:
       data[i] = new_string.count(i)
    return data


print(count_char(STR_VAL))
