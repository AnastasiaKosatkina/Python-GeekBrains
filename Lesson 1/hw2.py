numberofsecond = int(input('Введите количество секунд: '))
hour = (numberofsecond//3600)
minute = (numberofsecond - hour*3600)//60
second = numberofsecond - (hour*3600 + minute*60)

print(f"Время в формате чч:мм:сс   {hour:02} : {minute:02} : {second:02}")
