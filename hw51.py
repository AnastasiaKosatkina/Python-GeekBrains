''' Создать программно файл в текстовом формате, записать в него построчно данные,
вводимые пользователем. Об окончании ввода данных свидетельствует пустая строка.
'''

with open('user_text.txt', 'w') as ut:
    while True:
        user_str = input('If you want finish text " "')
        if user_str == ' ':
            break
        ut.write(user_str + '\n')
