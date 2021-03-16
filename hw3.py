'''Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
'''

def my_func(number_one, number_two, number_three):
   summe_max_two = [number_one, number_two, number_three]
   summe_max_two.remove(min(summe_max_two))
   return sum(summe_max_two)

summe_my_func = my_func(5, 7, 1)
print(summe_my_func)
