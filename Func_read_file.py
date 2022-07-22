# Функция присваивания строке содержимого файла Markdown

def read_file(user_file):
    with open(user_file, 'r', encoding='utf-8') as pol:
        polynom = pol.read()
        return polynom
