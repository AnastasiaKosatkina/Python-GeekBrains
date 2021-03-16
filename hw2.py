'''Реализовать функцию, принимающую несколько параметров, описывающих данные
пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.
'''

def user_profile(name, sername, birth_year, city, email, number_phone):
    data = (f'User_name: {name}, '
            f'User_sername: {sername}, '
            f'User_birth_year: {birth_year}, '
            f'User_city: {city}, '
            f'User_email: {email}, '
            f'User_number_phone: {number_phone}')
    # print(data)
    return data

key = user_profile('Ana', 'Ivanova', '1900', 'Samara', 'pochta@pocta.ru', '89009009090')
print(key)