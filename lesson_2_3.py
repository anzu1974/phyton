#3. Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить, к какому времени года относится месяц
# (зима, весна, лето, осень). Напишите решения через list и dict.

dict_data = {1 : 'Зима', 2 : 'Зима', 3 : 'Весна', 4 : 'Весна', 5 : 'Весна', 6 : 'Лето', 7 : 'Лето', 8 : 'Лето',
             9 : 'Осень', 10 : 'Осень', 11 : 'Осень', 12 : 'Зима'}
month = int(input('Введите номер месяца - '))
print(f'{month} это {dict_data.get(month)}')
#print(f'{month} это {dict_data[month]}')


list_data_vg = ('зима', 'весна', 'лето', 'осень')
list_data_num = [(12, 1, 2), (3, 4, 5), (6, 7, 8), (9, 10, 11)]

month = int(input('Введите номер месяца - '))
for i in range(4):
    if month in list_data_num[i]:
        print(list_data_vg[i])
#print(list(range(4)))


list_data = [('зима', 'весна', 'лето', 'осень'), (12, 1, 2), (3, 4, 5), (6, 7, 8), (9, 10, 11)]
month = int(input('Введите номер месяца - '))
if month in list_data[1]:
    print( list_data[0][0])
elif month in list_data[2]:
    print(list_data[0][1])
elif month in list_data[3]:
    print(list_data[0][2])
elif month in list_data[4]:
    print(list_data[0][3])
else:
    print('Такого времени года нет')








