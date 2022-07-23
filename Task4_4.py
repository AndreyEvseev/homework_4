# Задание 4. Задана натуральная степень k. Сформировать случайным образом список коэффициентов
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.

k = int(input('Задайте натуральную степень многочлена k: '))
import Func_coeff_polinom as cp 
coeff_polynom = cp.fill_coefficients_polynomial_list(k)
my_file = 'f_polinom4_4.txt'
import Func_call_record_func as fc
fc.call_record_func(k, coeff_polynom, my_file)
