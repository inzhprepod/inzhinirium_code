'''player1 = input('Ход первого игрока')
player2 = input('Ход второго игрока')

if player1 == 'камень' and player2 == 'камень':
    print('Ничья')
elif player1 == 'камень' and player2 == 'ножницы':
    print('Выиграл первый игрок')
'''

slovo = input('Введите слово:')

if len(slovo) > 3:
    print(slovo[3])
else:
    print('Нет')
