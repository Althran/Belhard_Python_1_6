"""
Написать композицию из функций (не чистых функций)

Имеется словарь SCHOOL_DATA с данными школы класс-количество учеников

- Функция incr_students, которая принимает SCHOOL_DATA, название класса и
    увеличивает количество учеников на 1
- Функция decr_students, которая принимает SCHOOL_DATA, название класса и
    уменьшает количество учеников на 1, но не меньше 0
- Функция add_class, которая принимает SCHOOL_DATA, название класса и добавляет
    класс в словарь с количеством учеников 0
- Функция remove_class, которая принимает SCHOOL_DATA, название класса и удаляет
    класс из словаря
- Функция calc_students, которая принимает SCHOOL_DATA и возвращает кол-во
    учеников во всей школе
"""
school_data = {
    '1a': 15,
    '1b': 23,
    '2a': 13,
    '2b': 30
}


def incr_students(data, name):
    if data[name][0] != 0:
        data[name] = data[name][0] + 1
    else:
        return data
    return data


def decr_students(data, name):
    data[name] = data[name][0] - 1
    return data


def add_class(data, new):
    data[new] = 0
    return data


def remove_class(data, name):
    del data[name]
    return data


def calc_students(data):
    summa = sum(data.values)
    return summa
