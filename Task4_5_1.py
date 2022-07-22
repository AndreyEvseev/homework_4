# Задание 5. Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов.

# В этом файле создаются файлы с многочленами для решения задачи (Task4_5.py)

k1 = int(input('Задайте натуральную степень 1-го многочлена k1: '))
k2 = int(input('Задайте натуральную степень 2-го многочлена k2: '))
import Func_coeff_polinom as cp 
coeff_polinom1 = cp.fill_coefficients_polynomial_list(k1, -90, 90)
coeff_polinom2 = cp.fill_coefficients_polynomial_list(k2, -90, 90)
# Запись многочленов в файлы. Доступна запись файлов типа .md или .txt
my_file1='f_polinom4_5_1.md' 
my_file2='f_polinom4_5_2.md' 
import Func_call_record_func as fc
fc.call_record_func(k1, coeff_polinom1, my_file1)
fc.call_record_func(k2, coeff_polinom2, my_file2)

# Выполнено условие "Даны два файла, в каждом из которых находится запись многочлена"
# Решение задачи - в файле "Task4_5.py"
