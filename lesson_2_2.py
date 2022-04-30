#2. Для списка реализовать обмен значений соседних элементов. Значениями обмениваются элементы с
# индексами 0 и 1, 2 и 3 и т. д. При нечётном количестве элементов последний сохранить на своём месте.
# Для заполнения списка элементов нужно использовать функцию input().
i = 0
els = []
n = int(input('Введите количество элементов - '))
while i < n:
    els.append(input(f'Введите {i} элемент списка - '))
    i = i + 1
print(els)

#els=list(input('Введите список цифр - '))
#print(els)
for index in range(1, len(els), 2):
    els.insert(index - 1, els[index])
    els.pop(index+1)
print(els)


m = len(els) if len(els) % 2 == 0 else len(els) - 1
for i in range(0, m, 2):
    els[i], els[i+1] = els[i+1], els[i]
print(els)