spisok = []

while True:
    chislo = input('Введите число: ')
    if chislo == '!':
        break
    if int(chislo) >= 160 and int(chislo) <= 180:
        spisok.append(chislo)

print(len(spisok))
print(max(spisok), min(spisok))