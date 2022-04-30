#Реализовать структуру «Рейтинг», представляющую собой набор натуральных чисел, который не возрастает.
# У пользователя нужно запрашивать новый элемент рейтинга. Если в рейтинге существуют элементы с одинаковыми значениями,
# то новый элемент с тем же значением должен разместиться после них.
#Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
#Пользователь ввёл число 3. Результат: 7, 5, 3, 3, 3, 2.
#Пользователь ввёл число 8. Результат: 8, 7, 5, 3, 3, 2.
#Пользователь ввёл число 1. Результат: 7, 5, 3, 3, 2, 1.
#Набор натуральных чисел можно задать сразу в коде, например, my_list = [7, 5, 3, 3, 2].

list_reitings = [7, 5, 3, 3, 2]
list_reiting = int(input('Введите новое значение рейтинга - '))

for i in range(len(list_reitings)):
    if list_reiting == list_reitings[i]:
        list_reitings.insert(list_reitings.index(list_reitings[i]) + list_reitings.count(list_reitings[i]), list_reiting)
        break
    elif list_reiting > list_reitings[i]:
        list_reitings.insert(list_reitings.index(list_reitings[i]), list_reiting)
        break


print(list_reitings)