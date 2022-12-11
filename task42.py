# 1. Создайте программу для игры с конфетами человек против человека.
# *' Условие задачи: На столе лежит 117 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. 
# За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход.

# a) Добавьте игру против бота

import random
candys = 117

def input_candy():
    global candys
    while True:
        move = int(input('Введите конфеты: '))
        if move > 0 and move < 29 and move <= candys:
            candys -= move
            break
        else:
            print('Столько конфет взять нельзя! Попробуйте ещё раз!')

def bot_take():
    global candys
    while True:
        move = random.randint(1, 28)
        if move > 0 and move < 29 and move <= candys:
            print(f'Бот взял {move} конфет')
            candys -= move
            break

print(f'На столе лежит {candys} конфет')
players = ['Пользователь', 'Компьютер']
move = random.choice(players)
print(f'Первым ходит - {move}')
while True:
    if move == 'Пользователь':
        input_candy()
        print(f'Осталось {candys}')
        move = 'Компьютер'
        if candys < 29:
            print(f'Победил {move}')
            break
    else:
        bot_take()
        print(f'Осталось {candys}')
        move = 'Пользователь'
        if candys < 29:
            print(f'Победитель {move}')
            break