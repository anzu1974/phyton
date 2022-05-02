#7. Продолжить работу над заданием. В программу должна попадать строка из слов, разделённых пробелом.
# Каждое слово состоит из латинских букв в нижнем регистре. Нужно сделать вывод исходной строки,
# но каждое слово должно начинаться с заглавной буквы. Используйте написанную ранее функцию int_func().

def int_func(stroka):
    return stroka.title()

def stroka_title(stroka):
    stroka_list = stroka.split(' ')
    titl_stroka = []
    for sl in stroka_list:
        titl_stroka.append(int_func(sl))

    return ' '.join(titl_stroka)
a = 'vova sveta misha sasha'
print(stroka_title(a))
print(a.title())
