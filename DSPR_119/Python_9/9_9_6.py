# Не забудьте импортировать numpy и сразу задать seed 2021
import numpy as np
np.random.seed(2021)
# В simple сохранте случайное число в диапазоне от 0 до 1
simple = None
simple = np.random.rand()
# Сгенерируйте 120 чисел в диапазоне от -150 до 2021, сохраните их
# в переменную randoms
randoms = None
randoms = np.random.uniform(-150, 2021, size=120)
# Получите массив из случайных целых чисел от 1 до 100 (включительно)
# из 3 строк и 2 столбцов. Сохраните результат в table
table = None
table = np.random.randint(1,101,size=(3,2))
# В переменную even сохраните четные числа от 2 до 16 (включительно)
even = None
even = np.array([2, 4, 6, 8, 10, 12, 14, 16])
# Перемешайте числа в even так, чтобы массив even изменился
np.random.shuffle(even)
# Получите из even 3 числа без повторений. Сохраните их в переменную select
select = None
select = np.random.choice(even, size=3,replace=False)
# Получите переменную triplet, которая должна содержать перемешанные
# значения из массива select (сам select измениться не должен)
triplet = None
triplet = np.random.permutation(select)