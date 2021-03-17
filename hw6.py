'''Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
Каждый кортеж хранит информацию об отдельном товаре. В кортеже должно быть два элемента —
номер товара и словарь с параметрами (характеристиками товара: название, цена, количество,
единица измерения). Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
Необходимо собрать аналитику о товарах. Реализовать словарь, в котором каждый ключ —
характеристика товара, например название, а значение — список значений-характеристик,
например список названий товаров.
'''

goods = []
structure = {'название':'', 'цена':'', 'количество':'', 'единица измерения':''}
statistics = {'название':[], 'цена': [], 'количество': [], 'единица измерения':[]}
order = 0
while True:
    if input('Если Вы хотите покинуть поле заполнения, нажмите E: ').upper() == 'E':
        break
    order += 1
    for s in structure.keys():
        new_data = input(f'{s}: ')
        structure[s]= int(new_data) if (s == 'цена' or s == 'количество') else new_data
        statistics[s].append(structure[s])
    goods.append((order, structure.copy()))
    print('Аналитика по товарам: \n')
    for key, value in statistics.items():
        print(key, value)
print(goods)
