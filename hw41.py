'''Реализовать скрипт, в котором должна быть предусмотрена функция расчёта
заработной платы сотрудника. Используйте в нём формулу:
(выработка в часах*ставка в час) + премия. Во время выполнения расчёта
для конкретных значений необходимо запускать скрипт с параметрами.
'''

import sys

def salary(hours, rate_hours, premium):
    return hours * rate_hours + premium

hours, rate_hours, premium = map(float, sys.argv[1:])
print(salary(hours, rate_hours, premium))