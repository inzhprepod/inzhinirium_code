'''pomidori = True
ogurci = False
smetana = False
luk = False

if pomidori or ogurci or smetana or luk:
    print('Сегодня будем есть салат')
else:
    print('Салата не будет')

kurica = True
suhari = True
salat = True
sir = True
sous = True

if kurica and suhari and salat and sir and sous:
    print('Цезарь сможем приготовить')
else:
    print('Цезарь не получится')
'''

stroka1 = input('Введите первую строку')
stroka2 = input('Введите вторую строку')
stroka3 = input('Введите третью строку')

if stroka1 == 'красный' and stroka2 == 'желтый' and stroka3 == 'зеленый' or \
    stroka1 == '3' and stroka2 == '2' and stroka3 == '1':
    print('Поехали')
else:
    print('Стой')
