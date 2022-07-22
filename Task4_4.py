# Задана натуральная степень k. Сформировать случайным образом список коэффициентов 
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.

def call_record_func(k: int, coeff_polinom: list, user_file: str):
    if user_file[-3:len(user_file)] == '.md':
        import Func_write_md as file
        file.writing_file_md(k, coeff_polinom, user_file)
    elif user_file[-4:len(user_file)] == '.txt':
        import Func_write_txt as file
        file.writing_file_txt(k, coeff_polinom, user_file)
    else:
        print('Не определён тип файла. Распознаются типы: .md и txt') 

k = int(input('Задайте натуральную степень многочлена k: '))
import Func_coeff_polinom as cp 
coeff_polynom = cp.fill_coefficients_polynomial_list(k)
my_file = 'f_polinom4_4.md'
call_record_func(k, coeff_polynom, my_file)
