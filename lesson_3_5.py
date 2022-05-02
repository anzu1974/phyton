#5. Программа запрашивает у пользователя строку чисел, разделённых пробелом. При нажатии Enter должна выводиться
# сумма чисел. Пользователь может продолжить ввод чисел, разделённых пробелом и снова нажать Enter. Сумма вновь
# введённых чисел будет добавляться к уже подсчитанной сумме.Но если вместо числа вводится специальный символ,
# выполнение программы завершается. Если специальный символ введён после нескольких чисел, то вначале нужно добавить
# сумму этих чисел к полученной ранее сумме и после этого завершить программу.


def my_numbers():
    numbers_sum = 0
    while True:
        str_numbers = input('Вводите числа через пробел - ')
        list_numbers = str_numbers.split(' ')
        numbers = []
        for list_number in list_numbers:
            try:
                number = int(list_number)
                #numbers.append(number)
            except:
                ValueError
                return numbers_sum + sum(numbers)
            numbers.append(number)
        numbers_sum = numbers_sum + sum(numbers)
        print(numbers_sum)




print(my_numbers())