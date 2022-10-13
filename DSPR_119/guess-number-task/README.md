# Проект 0. Угадай число 

## Оглавление  
[1. Описание проекта](https://github.com/inconstant1313/DSPR_119/tree/main/guess-number-task#%D0%BE%D0%BF%D0%B8%D1%81%D0%B0%D0%BD%D0%B8%D0%B5-%D0%BF%D1%80%D0%BE%D0%B5%D0%BA%D1%82%D0%B0)  
[2. Какой кейс решаем?](https://github.com/inconstant1313/DSPR_119/tree/main/guess-number-task#%D0%BA%D0%B0%D0%BA%D0%BE%D0%B9-%D0%BA%D0%B5%D0%B9%D1%81-%D1%80%D0%B5%D1%88%D0%B0%D0%B5%D0%BC)  
[3. Краткая информация о данных](https://github.com/inconstant1313/DSPR_119/tree/main/guess-number-task#%D0%BA%D1%80%D0%B0%D1%82%D0%BA%D0%B0%D1%8F-%D0%B8%D0%BD%D1%84%D0%BE%D1%80%D0%BC%D0%B0%D1%86%D0%B8%D1%8F-%D0%BE-%D0%B4%D0%B0%D0%BD%D0%BD%D1%8B%D1%85)  
[4. Этапы работы над проектом](https://github.com/inconstant1313/DSPR_119/tree/main/guess-number-task#%D1%8D%D1%82%D0%B0%D0%BF%D1%8B-%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D1%8B-%D0%BD%D0%B0%D0%B4-%D0%BF%D1%80%D0%BE%D0%B5%D0%BA%D1%82%D0%BE%D0%BC)  
[5. Результат](https://github.com/inconstant1313/DSPR_119/tree/main/guess-number-task#%D1%80%D0%B5%D0%B7%D1%83%D0%BB%D1%8C%D1%82%D0%B0%D1%82%D1%8B)    
[6. Выводы](https://github.com/inconstant1313/DSPR_119/tree/main/guess-number-task#%D0%B2%D1%8B%D0%B2%D0%BE%D0%B4%D1%8B) 

### Описание проекта    
Угадать загаданное компьютером число за минимальное число попыток. При этом попыток не должно быть больше 20.

### Какой кейс решаем?    
Нужно написать программу, которая угадывает число, при этом тратит на это менее 20 попыток.

**Условия соревнования:**  
- Компьютер загадывает целое число от 1 до 100, и нам его нужно угадать. Под «угадать», подразумевается «написать программу, которая угадывает число».
- Алгоритм учитывает информацию о том, больше ли случайное число или меньше нужного нам.

**Метрика качества**     
Результаты оцениваются по среднему количеству попыток при 1000 повторений. Необходимо добиться минимального количества попыток.

**Что практикуем?**     
- Учимся писать хороший код на Python.
- Учимся работать с IDE.
- Учимся работать с GitHub.


### Краткая информация о данных
....

:arrow_up:[к оглавлению](https://github.com/inconstant1313/DSPR_119/tree/main/guess-number-task#%D0%BE%D0%B3%D0%BB%D0%B0%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5)

### Этапы работы над проектом  
1. Изучили работу базовых решений ([game.py](https://github.com/inconstant1313/DSPR_119/blob/main/guess-number-task/game.py) и [game_v2.py](https://github.com/inconstant1313/DSPR_119/blob/main/guess-number-task/game_v2.py)).
2. Изучили простые методы поиска в массиве(диапазоне) чисел. Выбрали подходящий метод (Binary search).
3. Внесли изменения в код [game_v2.py](https://github.com/inconstant1313/DSPR_119/blob/main/guess-number-task/game_v2.py) согласно выбранному методу. Сохранили результат в [game_v3.py](https://github.com/inconstant1313/DSPR_119/blob/main/guess-number-task/game_v3.py)
4. Проверили, что число попыток сократилось до необходимого количества. Также проверили, что при увеличении количества проходов результат сохраняется.

:arrow_up:[к оглавлению](https://github.com/inconstant1313/DSPR_119/tree/main/guess-number-task#%D0%BE%D0%B3%D0%BB%D0%B0%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5)


### Результаты:  
Среднее количество попыток при использовании Binary search algorithm сокращается до 5-6 попыток.

:arrow_up:[к оглавлению](https://github.com/inconstant1313/DSPR_119/tree/main/guess-number-task#%D0%BE%D0%B3%D0%BB%D0%B0%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5)


### Выводы:  
Использование Binary search algorithm сокращает количество попыток в среднем на 95% в сравнении с методом рандомного подбора.

:arrow_up:[к оглавлению](https://github.com/inconstant1313/DSPR_119/tree/main/guess-number-task#%D0%BE%D0%B3%D0%BB%D0%B0%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5)