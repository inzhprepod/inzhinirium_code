'''state = input('Как себя чувствуешь?')
if state == 'хорошо':
    print('Иди погуляй')
    print('Только будь осторожным')
    print('Надень шапку')
elif state == 'болит живот':
    print('Выпей таблетку')
else:
    print('Ложись спать')
'''

'''
print('Привет')# 1 пункт

# 2 пункт
name = input('Введите имя:')
surname = input('Введите фамилию:')
age = int(input('Введите возраст:'))

# 3 пункт
if age >= 18:
    print('Ты уже взрослый')
else:
    print('Ты еще ребенок')
'''

vopros1 = input('Пойдешь гулять?')
if vopros1 == 'да':
    print('Хорошо, тогда сегодня в 16:00')
elif vopros1 == 'нет':
    print('Ладно, значит в следующий раз')
else:
    print('Ошибка')

vopros2 = input('Пойдешь в кино?')
if vopros2 == 'да':
    print('Я тоже пойду')
elif vopros2 == 'нет':
    print('Жаль, мы все идем')
else:
    print('Ошибка')