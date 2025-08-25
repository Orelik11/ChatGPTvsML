import numpy as np

arr = np.array([[1, 2, 3],
                [4, 5, 6]])

print(arr + 10)
# [[11 12 13]
#  [14 15 16]]

row_vec = np.array([10, 20, 30])
print(arr + row_vec)
# [[11 22 33]
#  [14 25 36]]

col_vec = np.array([[100],
                    [200]])
print(arr + col_vec)
# [[101 102 103]
#  [204 205 206]]


arr = np.array(
    [1,2,3,100],
    [4,5,6,200],
    [7,8,9,300],
)

print(arr+5)
row_vec = np.array([4,5,6,7])
print(arr+row_vec)
col_vec = np.array(
    [10],
    [20],
    [30])
print(arr + col_vec)