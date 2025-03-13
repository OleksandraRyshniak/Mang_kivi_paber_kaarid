import os
import subprocess
import random
while True:
    print("Привет! Хочешь сыграть в игру камень, ножницы, бумага: ")
    mäng=input("Jah või Ei: ")
    if mäng=="Jah": 
        robot_list=['kivi', 'käärid', 'paber' ]
        rounds=int(input("Сколько раундов ты хочешь сыграть: "))
        score={"Player" : 0 , "Robot" : 0}
        score2={"Player_1" : 0 , "Player_2" : 0}
        while 1:
            try:
                player=input("С кем ты хочешь сыграть?(выбери с роботом или с другом):  ")
                if player.isalpha(): break
            except:
                print("выбери с роботом или с другом!")
            while 1:
                    if player=="с роботом" or player=="с другом": 
                        if player=="с роботом":
                            my_list=input("Введите свой список (например: ['бумага', 'ножницы', ... ]): ")
                            for i in range (rounds):
                                print(f"{i+1} раунд: ")
                                while 1:
                                    try:
                                        player_valik=str(input("Введи одно значение из своего списка: "))
                                        if player_valik.isalpha(): break
                                        if player_valik in robot_list:
                                            break
                                        else:
                                            print("Вводите только слова из списка!")
                                    except:
                                        print("Вводите только буквы!")
                                if player_valik=="paber" or player_valik=="käärid" or player_valik=="kivi":
                                    valik_robot=random.choice(robot_list)
                                    print(f"player_1: {player_valik}, robot: {valik_robot}")
                                if (player_valik=="paber" and valik_robot=="kivi") or\
                                (player_valik=="kivi" and valik_robot=="käärid") or\
                                (player_valik=="käärid" and valik_robot=="paber"):
                                    score["Player"] +=1
                                    print(f"Выграл: player_1")
                                elif (valik_robot=="kivi" and player_valik=="käärid") or\
                                     (valik_robot=="paber" and player_valik=="kivi") or \
                                     (valik_robot=="käärid" and player_valik=="paber"):
                                    score["Robot"] +=1
                                    print("Выграл робот")
                                elif valik_robot==player_valik:
                                    print("Ничья")
                                else:
                                    print("Вводите только камень, ножницы , бумага!")
                                print(f"Счёт - {score["Player"]}  {score["Robot"]}")
                        elif player=="с другом": 
                            my_list1=input("Первый игрок вводит свой список (например: ['бумага', 'ножницы', ... ]): ")
                            os.system("cls")
                            my_list2=input("Второй игрок вводит свой список (например: ['бумага', 'ножницы', ... ]): ")
                            os.system('cls' if os.name == 'nt' else 'clear')
                            for i in range (rounds):
                                print(f"{i+1} раунд: ")
                            while 1:
                                    try:
                                        player_valik=str(input("Игрок 1 введи одно значение из своего списка: "))
                                        if player_valik.isalpha(): break
                                        if player_valik in robot_list:
                                            break
                                        else:
                                            print("Вводите только слова из списка!")
                                    except:
                                        print("Вводите только буквы!")
                            while 1:
                                    try:
                                        player_valik2=str(input("Игрок 2 введи одно значение из своего списка: "))
                                        if player_valik2.isalpha(): break
                                        if player_valik2 in robot_list:
                                            break
                                        else:
                                            print("Вводите только слова из списка!")
                                    except:
                                        print("Вводите только буквы!")
                            if (player_valik=="paber" or player_valik=="käärid" or player_valik=="kivi"):
                               print(f"player_1: {player_valik}, player_2: {player_valik2}")
                               if (player_valik=="paber" and player_valik2=="kivi") or\
                                        (player_valik=="kivi" and player_valik2=="käärid") or\
                                        (player_valik=="käärid" and player_valik2=="paber"):
                                        score2["Player_1"] +=1
                                        print(f"Выграл: player_1")
                               elif (player_valik2=="kivi" and player_valik=="käärid") or\
                                        (player_valik2=="paber" and player_valik=="kivi") or \
                                        (player_valik2=="käärid" and player_valik=="paber"):
                                        score2["Player_2"] +=1
                                        print("Выграл player_2")
                               elif player_valik2==player_valik:
                                        print("Ничья")
                            print(f"Счёт - {score2["Player"]}  {score2["Player_2"]}")
                        else:
                            print("Напиши только 'с роботом' или 'с другом'!")
                    else:
                        print("Напиши только 'с роботом' или 'с другом'!")
            break
    elif mäng=="Ei":
        print("До встречи")
        break
    else:
        print("Введите только Да или Нет!")

