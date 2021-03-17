''' Для списка реализовать обмен значений соседних элементов, т.е.
 Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
 При нечетном количестве элементов последний сохранить на своем месте.
 Для заполнения списка элементов необходимо использовать функцию input().
'''

personal_random = list(input('Введите текст: '))
for i in range(1, len(personal_random), 2):
    personal_random[i - 1], personal_random[i] = personal_random[i], personal_random[i -1]
    print(personal_random)