import numpy as np

arr = np.array([[10, 20, 30],
                [40, 50, 60],
                [70, 80, 90]])

# Доступ к одному элементу
print(arr[0, 1])  # 20 (первая строка, второй столбец)

# Срез строки
print(arr[1])     # [40 50 60]

# Срез столбца
print(arr[:, 2])  # [30 60 90]

# Срез подмассива
print(arr[0:2, 1:3])  
# [[20 30]
#  [50 60]]

# print(arr[2])
# print(arr[:, 2])
# print(arr[2, 0])



print('-------------------')
arr = np.array([[10,    20,     30,     40],
                [50,    60,     70,     80],
                [90,    100,    110,    120],
                [130,   140,    150,    160]])

print(f'print first line\n {arr[0]}')
print(f'print last column:\n {arr[:,-1]}')
print(f'submatrix 2x2 from center\n {arr[1:3, 1:3]}')