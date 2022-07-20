# Задана натуральная степень k. Сформировать случайным образом список коэффициентов 
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.

import random

def fill_coefficients_polynomial_list(k, min=0, max=100) -> list:
    new_list = [random.randint(min, max)]
    while new_list[0] == 0:
        new_list[0] = random.randint(min, max)
    for i in range (1, k+1):
        new_list.append(random.randint(min, max)) 
    return new_list

def conversion_to_string_md(k: int, user_list):
    if user_list[0] == 1:
        num = '$'
    else:
        num = f'${user_list[0]}'
    polynom = f'{num}x^{k}'
    for i in range(1,k+1):
        if user_list[i] != 0:
            if user_list[i] > 0:
                sign = '+'
            else:
                sign = ''
            if user_list[i] == 1:
                num = ''
            else:
                num = f'{user_list[i]}'            
            if i != k and i != k-1:
                polynom = polynom + f'{sign}{num}x^{k-i}'
            elif i == k-1:
                polynom = polynom + f'{sign}{num}x'
            else:
                polynom = polynom + f'{sign}{user_list[i]}'
    polynom = polynom + '=0$'
    return polynom

def writing_file_md(polynom_str: str, user_file: str):
    with open(user_file, 'w', encoding='utf-8') as pol:
        pol.writelines(polynom_str)

def read_file_md(user_file):
    with open(user_file, 'r', encoding='utf-8') as pol:
        polynom = pol.read()
        return polynom    

k = int(input('Задайте натуральную степень многочлена k: '))
coeff_polynom = fill_coefficients_polynomial_list(k)
print(coeff_polynom)
polynom_str = conversion_to_string_md(k, coeff_polynom)
my_file = 'file4_4.md'
writing_file_md(polynom_str, my_file)
polynom = read_file_md(my_file)
print(polynom)


