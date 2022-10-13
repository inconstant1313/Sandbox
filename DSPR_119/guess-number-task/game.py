"""Игра угадай число"""

import numpy as np

def random_game():
    number = np.random.randint(1, 101) # загадываем число

    # количество попыток
    count = 0

    while True:
        count+=1
        predict_number = int(input("Угадай число от 1 до 100: "))
    
        if predict_number > number:
            print("Число должно быть меньше!")

        elif predict_number < number:
            print("Число должно быть больше!")
    
        else:
            print(f"Вы угадали число! Это число = {number}, за {count} попыток")
            break #конец игры выход из цикла
    return("You win!!!")    

#print(random_game()) # для запуска игры из этого файла уберите #
