'''Создать (не программно) текстовый файл со следующим содержимым:
Необходимо написать программу, открывающую файл на чтение и считывающую
построчно данные. При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.'''

with open('enghw4.txt', encoding='utf-8') as f:
    lines = f.readlines()

with open('ruhw4.txt', 'w', encoding='utf-8') as f:
    for number in lines:
        if '1' in number:
            number = number.replace('One', 'Один')
        elif '2' in number:
            number = number.replace('Two', 'Два')
        elif '3' in number:
            number = number.replace('Three', 'Три')
        elif '4' in number:
            number = number.replace('Four', 'Четыре')
        f.write(number)