# Функция для конвертации списка коэффициентов многочлена в строку 
# для записи в файл Markdown

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
