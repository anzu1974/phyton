#2. Выполнить функцию, которая принимает несколько параметров, описывающих данные пользователя: имя, фамилия,
# год рождения, город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы.
# Осуществить вывод данных о пользователе одной строкой.

def info_client(name, sec_name, dr, city, e_mail, tel):
    list_info_client = f'{name} {sec_name} {dr} года рождения проживает в {city}, e-mail: {e_mail}, тел. {tel}'
    return list_info_client


print(info_client(name='Piter', city='Moscow', dr=2000, e_mail='xxx@yandex.ru', tel='+7 999 999 9999',
                  sec_name='Popov'))

