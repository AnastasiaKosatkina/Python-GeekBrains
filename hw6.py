start = int(input('Введите результат первого дня (в км): '))
target = int(input('Введите минимальный общий результат (в км): '))
day = int(1)

while target > start:
        start = start + 0.1 * start
        day += 1

print('На ' + str(int(day)) + '-й день спортсмен достиг результата — не менее ' + str(int(target)) + ' км.')