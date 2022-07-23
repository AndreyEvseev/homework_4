# Задание 7. В файле находится N натуральных чисел, записанных через пробел. 
# Среди чисел не хватает одного, чтобы выполнялось условие A[i] - 1 = A[i-1]. Найти его.

import random

def file_generator(user_file, n: int):
    exception = random.randint(1, N-1)
    min = random.randint(10, 50)
    with open(my_file, 'w', encoding='utf-8') as num:
        for i in range(min, min+N+1):
            if i != min+N+1:
                if i != min+exception:
                    num.write(f'{i} ')
            elif i == min+N+1:
                num.write(f'{i}')

def str_to_int_list(p: str) -> list:
    n = []
    while len(p) > 0:
        if p.find(' ') != -1:
            if p[0] == '':
                p = p[:0] + p[1:]
            else:
                n.append(int(p[:p.index(' ')]))
                p = p[:0] + p[p.index(' ') + 1:]
        else:
            n.append(int(p[:len(p)]-1))
    return n

def find_loss(s: list) -> int:
    for i in range(1, len(s)):
        if s[i] - 1 != s[i-1]:
            loss = s[i] - 1
    return loss

N = 11
my_file = 'f_numbers4_7.txt'
file_generator(my_file, N)

import Func_read_file as rf
sequence = rf.read_file(my_file)
s1 = str_to_int_list(sequence)
loss = find_loss(s1)
print(f'Чтобы выполнялось условие A[i]-1 = A[i-1], \n'
    f'в заданной последовательности [ {sequence}] не хватает числа {loss}')

