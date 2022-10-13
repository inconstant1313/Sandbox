'''Напишите функцию get_unique_loto(num). 
Она так же, как и функция в задании 10.10, 
генерирует num полей для игры в лото, 
однако теперь на каждом поле 5х5 числа не могут повторяться.
Функция также должна возвращать массив формы num x 5 x 5.'''

import numpy as np

def get_unique_loto(num):
    result = np.arange(num*5*5).reshape(num, 5, 5)
    for i in range(num):
        numbers = np.arange(1,101)
        ticket = np.random.choice(numbers,size=(5,5), replace=False)
        result[i] = ticket
        i += 1
    return result
    
print(get_unique_loto(3))