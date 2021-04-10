'''Создать текстовый файл (не программно), построчно записать фамилии
сотрудников и величину их окладов. Определить, кто из сотрудников имеет
оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.
'''

with open('datahw53.txt') as hw3:
    lines = hw3.readlines()
    data = []
    for l in lines:
        ls = l.split(',')
        if float(ls[1]) < 20000:
            print(ls[0])
            data.append(ls[1].strip())
    print(f'Average salary: {sum(map(float, data))/len(data)}')