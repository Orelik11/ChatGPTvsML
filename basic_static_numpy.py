import numpy as np

np.random.seed(42)  # для воспроизводимости
arr = np.random.randint(0, 100, size=(5,5))
print(f'array: \n{arr}')

# общие характеристики
print("сумма всех элементов: ", arr.sum())
print("Среднее значение: ", arr.mean())
print("Максимальное значение: ", arr.max())
print("Минимальное значение: ", arr.min())
print("Стандартное отклонение: ", arr.std())

# Позиции элементов
print("Индекс минимального:", arr.argmin())  # одномерный индекс
print("Индекс максимального:", arr.argmax())

# По осям (очень важно!)
print("Сумма по строкам:", arr.sum(axis=1))
print("Сумма по столбцмам:", arr.sum(axis=0))
print("Среднее по столбцам:", arr.mean(axis=0))
print("Максимум по строкам:", arr.max(axis=1))


print('home work')
# домашнее задание
# Создай массив 10×10 случайных чисел (от 0 до 1, равномерное распределение).
arr_hw = np.random.rand(10, 10)
print(f'array: \n{arr_hw}')
# Найди среднее значение всех элементов.
print("Среднее значение: ", arr_hw.mean())
# среднее по каждой строке;
print("Среднее по строкам:", arr_hw.mean(axis=1))
# среднее по каждому столбцу;
print("Среднее по столбцам:", arr_hw.mean(axis=0))
# максимальное значение в каждом столбце;
print("Максимум по столбцам:", arr_hw.max(axis=0))

# Определи координаты глобального максимума (и сам элемент).
max_index = arr_hw.argmax()
max_value = arr_hw.max()
row, col = np.unravel_index(max_index, arr_hw.shape)
print(f"Глобальный максимум: {max_value} на позиции ({row}, {col})")