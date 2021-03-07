number = int(input('Введите целое положительное число: '))
maxnumber = number % 10
while number > 0:
    if number % 10 > maxnumber:
        maxnumber = number % 10
    number = number//10
print('Самая большая цифра в числе: ' + str(int(maxnumber)))
