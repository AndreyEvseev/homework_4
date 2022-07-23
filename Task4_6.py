# Задание 6. Создать текстовый файл (не программно). 
# Построчно записать фамилии сотрудников и величину их окладов (не менее 10 строк). 
# Определить, кто из сотрудников имеет оклад менее 20 тысяч, вывести фамилии этих сотрудников. 
# Выполнить подсчёт средней величины дохода сотрудников.

my_file = 'f_staff_list4_6.txt'

import Func_read_file as rf
source_staff_list = rf .read_file(my_file)
staff_list1 = source_staff_list.replace(',', '.')
staff_list1 = staff_list1.replace(' ', '\n')
staff_list = []
for element in staff_list1.split('\n'):
    staff_list.append(element)
for i in range(1, len(staff_list), 2):
    staff_list[i] = float(staff_list[i])
threshold = 20000
low_paid = []
print(f'Список сотрудников, получающих менее {threshold} рублей в месяц:')
for i in range(1, len(staff_list), 2):
    if staff_list[i] < threshold:
        low_paid.append(staff_list[i-1])
        print(staff_list[i-1])
sum, count = 0, 0
for i in range(1, len(staff_list), 2):
    sum += staff_list[i]
    count += 1
sum /= count
print(f'Средняя заработная плата сотрудников составляет {round(sum, 2)} рублей в месяц.')