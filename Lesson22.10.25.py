'''slovo1 = 'qweasd'
slovo2 = 'asdzxcghk'
while True:
    slovo1 = input('Введите первое слово: ')
    slovo2 = input('Введите второе слово: ')
    if slovo1[-1] == slovo2[0]:
        print('Правильно')
    else:
        print('Ошибка')
        break
'''

name = input('Введите имя:')
surname = input('Введите фамилию:')
age = int(input('Введите возраст:'))
print('Привет, ',name, surname)
print('Поздравляю с днем рождения')
age = age + 1
print('Тебе теперь', age, 'лет')
