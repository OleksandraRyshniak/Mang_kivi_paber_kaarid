
import random
while True:
    print("Привет! Хочешь сыграть в игру камень, ножницы, бумага: ")
    mäng=input("Jah või Ei: ")
    if mäng=="Jah": 
        robot_list=['kivi', 'käärid', 'paber' ]
        while 1:
            try:
                player_1=input("Введи своё имя: ")
                if player_1.isalphs():break
            except:
                print("Вводите только буквы!")
        rounds=int(input("Сколько раундов ты хочешь сыграть: "))
        player1=0
        robot=0
        player=input("С кем ты хочешь сыграть?(выбери с роботом или с другом):  ")
        if player=="с роботом":
            print("Какой сложности ты хочешь игру (выбери 1, 2): ")
            keerukus=int(input("Сложность: "))
            if keerukus==1:
                my_list=print(input("Введите свой список (например: ['бумага', 'ножницы', ... ]): "))
                for i in range (rounds):
                    print(f"{i+1}раунд: ")
                    while 1:
                        try:
                            player_valik=input("Введи одно значение из своего списка: ")
                            if player_valik.isalpha(): break
                        except:
                            print("Вводите только буквы!")
                    while 1:
                        if player_valik=="paber" or player_valik=="käärid" or player_valik=="kivi":
                            valik_robot=random.choise(robot_list)
                            print(f"{player_1}: {player_valik}, robot: {valik_robot}")

                            break
                        else:
                            print("Вводите только paber, käärid, kivi !")
            elif keerukus==2:
                my_list=print(input("Введите свой список (список вводиться так: ['слово1', 'слово2', ... ]): "))
            else:
                print("Введите только 1 или 2 !")
        elif player=="с другом": 
            print()
        else:
            print("Напиши только 'с роботом' или 'с другом'!")
        break
    elif mäng=="Ei":
        print("До встречи")
        break
    else:
        print("до встречи!")

