from os import system
import time

system('clear')
print('''Добро пожаловать в игру "крестики-нолики"!
Поле состоит из 9 клеток, каждая из которых
по умолчанию именована следующим образом:

-------------
| 1 | 2 | 3 |
-------------
| 4 | 5 | 6 |
-------------
| 7 | 8 | 9 |
-------------

Игрок 1 по умолчанию вводит "х", а игрок 2 - "о".
Для установки крестика "х" или нолика "о"
просто выберите номер поля и всё! :-)

Удачи ;-)\n''')

def CheckNumbers(param):
    while True:
        try:
            number = int(input(f"{param} "))
            if number >=1 and number <= 9:
                return number
            else: print("Число введено неправильно.")
        except:
            print("Число введено неправильно.")

def CheckWinner(array):
    status = False
    if array[0] == array[1] == array[2] != " ":
        status = True
    elif array[3] == array[4] == array[5] != " ":
        status = True
    elif array[6] == array[7] == array[8] != " ":
        status = True
    elif array[0] == array[4] == array[8] != " ":
        status = True
    elif array[2] == array[4] == array[6] != " ":
        status = True
    elif array[0] == array[3] == array[6] != " ":
        status = True
    elif array[1] == array[4] == array[7] != " ":
        status = True
    elif array[2] == array[5] == array[8] != " ":
        status = True
    return status

def PrintMap(a):
    print("-------------")
    print(f"| {a[0]} | {a[1]} | {a[2]} |")
    print("-------------")
    print(f"| {a[3]} | {a[4]} | {a[5]} |")
    print("-------------")
    print(f"| {a[6]} | {a[7]} | {a[8]} |")
    print("-------------")

for i in range(15, 0, -1):
    print(f'Через {i} секунд окно приветствия закроется..', end='')
    print('\r', end='')
    time.sleep(1)
system('clear')
player = 1
i = 1
a = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
while i <= 9:
    PrintMap(a)
    choice = CheckNumbers(f"\nИгрок {player}, введите номер клетки для заполнения:")
    if a[choice - 1] != " ":
        print("Такая клетка уже заполнена!")
        time.sleep(1)
        system('clear')
        continue
    else:
        if player == 1:
            a[choice - 1] = "x"
            player = 2
        else:
            a[choice - 1] = "o"
            player = 1
    if CheckWinner(a) == True:
        system('clear')
        PrintMap(a)
        if player == 1: player = 2
        else: player = 1
        print(f"\nИгрок {player} выиграл!\nПоздравляем с победой!")
        break
    i += 1
    system('clear')
if CheckWinner(a) == False:
    PrintMap(a)
    print("\nЧто ж, победителя нет... Может, сыграем еще? :-)")