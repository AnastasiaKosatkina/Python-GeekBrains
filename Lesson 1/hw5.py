income = int(input('Введите значение прибыли: '))
costs = int(input('Введите значение издержек: '))
profit = income-costs
profitability = profit/income

if income >= costs:
   print('Вы работаете с прибылью:' + str(int(profit)))
   print('Рентабельность вашей работы: ' + str(float(profitability)))
   employees = int(input('Введите численность сотрудников: '))
   profitonemloyees = int(profit/employees)
   print('Прибыль фирмы в расчете на одного сотрудника: ' + str(int(profitonemloyees)))
else:
    print('Вы работаете с убытком:' + str(int(profit)))

