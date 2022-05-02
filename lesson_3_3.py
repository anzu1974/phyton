#3. Реализовать функцию my_func(), которая принимает три позиционных аргумента и
# возвращает сумму наибольших двух аргументов.

def my_func(number_1, number_2, number_3):
    list_123 = [number_1, number_2, number_3]
    return sum(list_123) - min(list_123)

def my_func_sum_2(num_1, num_2, num_3):
    list_num = [num_1, num_2, num_3]
    list_num = sorted(list_num)
    return list_num[-1] + list_num[-2]

print(my_func(458, 228, 158))
print(my_func_sum_2(458, 228, 158))
