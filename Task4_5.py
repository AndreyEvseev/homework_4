# Задание 5. Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов.

# В этом файле решается задача формирования файла, содержащего сумму многочленов.
# Создание файлов с исходными многочленами выполняется в файле "Task4_5_1.py"

def transform_polinom(user_polynom: str, user_file: str):
    polyn = user_polynom.replace('$', '')
    polyn = polyn.replace(' ', '')
    polyn = polyn[:-2]
    return polyn

my_file1='f_polinom4_5_1.md' # Файл c записью 1-го многочлена
my_file2='f_polinom4_5_2.md' # Файл c записью 2-го многочлена

import Func_read_file as r
polynom1 = r.read_file(my_file1)
polynom2 = r.read_file(my_file2)

p1 = transform_polinom(polynom1, my_file1)
p2 = transform_polinom(polynom2, my_file2)
print(type(p1))
import Func_fill_missing_coeff as fm
tp1 = fm.fill_missing_coeff(p1)
tp2 = fm.fill_missing_coeff(p2)

import Func_sum_polinom as fs
result = fs.sum_polinom(tp1, tp2)

my_file_result='f_polinom4_5_result.txt' 
import Func_call_record_func as fc
fc.call_record_func(len(result)-1, result, my_file_result)
