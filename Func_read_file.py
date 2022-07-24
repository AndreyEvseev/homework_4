# Функция присваивания строке содержимого текстового файла

def read_file(user_file):
    with open(user_file, 'r', encoding='utf-8') as pol:
        result = pol.read()
        return result
