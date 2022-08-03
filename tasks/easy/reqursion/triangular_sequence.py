"""
Написать функцию triangular_sequence, которая принимает n и возвращает
последовательность следующего вида:

1
22
333
4444
55555
...

Например:

n = 3:
1
22
333

n = 6:
1
22
333
4444
55555
666666
"""


def triangular_sequence(n):
    if n == 0:
        return
    else:
        triangular_sequence(n - 1)
        print(str(n) * n, end='')
        print("\r")


triangular_sequence(6)
