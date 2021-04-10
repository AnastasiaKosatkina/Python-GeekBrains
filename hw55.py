'''Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.'''

with open('numbers.txt', 'w+', encoding='utf-8') as hw5:
    hw5.write(input('Enter a lot of numbers: '))
    hw5.tell()
    hw5.seek(0)
    l = hw5.read().split(' ')
    print(sum(map(float, l)))