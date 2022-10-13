"""Игра "Угадай число"
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np


def binary_predict(number: int = 1) -> int:
    """Угадываем число меньше, чем за 20 попыток, используя Двоичный поиск

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0 # переменная для хранения числа попыток
    first_value = 1 # начало диапазона возможных чисел
    last_value = 101 # конец диапазона возможных чисел

    while True:
        count += 1
        
        predict_number =  int((last_value - first_value)/2) # предполагаемое число
        
        if number < predict_number: 
            last_value = predict_number # переопределяем конец диапазона поиска
            
        if number > predict_number:
            first_value = -(predict_number) # переопределяем начало диапазона поиска
                 
        if number == predict_number:
            break  # выход из цикла, если угадали
    return count


def score_game(binary_predict) -> int:
    """Определяем какое количество попыток требуется алгоритму для поиска решения при 1000 проходов

    Args:
        binary_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    random_array = np.random.randint(1, 101, size=(1000))  # загадываем список чисел

    for number in random_array:
        count_ls.append(binary_predict(number)) # получаем список попыток по каждому числу

    score = int(np.mean(count_ls)) # вычисляем среднее количество попыток
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток.")
    return score


if __name__ == "__main__":
    # RUN
    score_game(binary_predict)