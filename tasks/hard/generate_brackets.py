"""
Задача из собеседования в яндекс

Написать рекурсивную функцию generate_brackets, которая принимает длину -
количество пар скобок, и будет генерировать все возможные варианты
скобочных последовательностей


Например:
generate_brackets(3)
n = 3
((()))
(()())
(())()
()(())
()()()

n = 4
(((())))
((()()))
((())())
((()))()
(()(()))
(()()())
(()())()
(())(())
(())()()
()((()))
()(()())
()(())()
()()(())
()()()()
"""


def generate_brackets(count, s='', left=0, right=0):
    if left == count and right == count:
        print(s)
    else:
        if left < count:
            generate_brackets(count, s + '(', left+1, right)
        if right < left:
            generate_brackets(count, s + ')', left, right+1)


generate_brackets(int(input()))
