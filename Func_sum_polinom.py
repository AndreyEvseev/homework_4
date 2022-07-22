# Функция суммирования двух многочленов

def addition_coefficients(user_polinom: list, complimentary: int) -> list:
    for i in range(complimentary):
        user_polinom.insert(0, 0)
    return user_polinom

def sum_polinom(tp1: list, tp2: list) -> list:
    if len(tp1) != len(tp2):
        complementary = abs(len(tp1) - len(tp2))
        if len(tp1) < len(tp2):
            tp1 = addition_coefficients(tp1, complementary)
        else:
            tp2 = addition_coefficients(tp2, complementary)    
    print(f'{tp1=}')
    print(f'{tp2=}')
    result = []
    for i in range(len(tp1)):
        result.append(tp1[i] + tp2[i])
    print(f'{result=}')
    return result

