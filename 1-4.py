
n = input('Введите любое число ')
d = list(n)
#maks = int(max(d))
#print(maks)
#print(d)
i = 0
maks = 0
while i < len(d):
    if int(d[i]) > maks:
        maks = int(d[i])
    i+=1

print(maks)




