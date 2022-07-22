# Функция для создания случайным образом списка коэффициентов многочлена

import random

def fill_coefficients_polynomial_list(k, min=0, max=100) -> list:
    new_list = [random.randint(min, max)]
    while new_list[0] == 0:
        new_list[0] = random.randint(min, max)
    for i in range (1, k+1):
        new_list.append(random.randint(min, max)) 
    return new_list
