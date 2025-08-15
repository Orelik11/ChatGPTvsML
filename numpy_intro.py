import numpy as np

# array 1-dimentional
arr1 = np.array([1,2,3,4])

print("arr1:", arr1)
print(f"type data: {arr1.dtype}")
print(f"dimentional shape: {arr1.shape}")

# Векторная операция (без циклов!)
print("\narr1 + 10:", arr1 + 10)
print("arr1 * 2:", arr1 * 2)

# Арифметика между массивами
arr3 = np.array([10, 20, 30, 40])
print("arr1 + arr3:", arr1 + arr3)


arr31 = np.array([  [1,2,3],
                    [1,2,3],
                    [1,2,3]])
arr32 = np.array([
    [1,2,3],
    [1,2,3],
    [1,2,3]])

print(f"arr31 * arr32: \n{arr31 * arr32}")
print(f"arr31 + arr32: \n{arr31 + arr32}")
print(f"shape dimentional arr31 + arr32: \n{(arr31 + arr32).shape}")