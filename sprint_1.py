from dataclasses import dataclass
import numpy as np
import pandas as pn


# Typical class
class Dog:
    def __init__(self, dog_name, dog_old, dog_color):
        self.dog_name = dog_name
        self.dog_old = dog_old
        self.dog_color = dog_color

    def __str__(self):
        return str(self.dog_name) + ' ' + str(self.dog_old) + ' ' + str(self.dog_color)

    def __eq__(self, other):
        if self.dog_color == other.dog_color and self.dog_name == other.dog_name and self.dog_old == other.dog_old:
            return True
        else:
            return False


# Data class
@dataclass
class Cat:
    cat_name: str
    cat_old: int
    cat_color: str


dog1 = Dog('Sharik', 4, 'Black')
dog2 = Dog('Sharik', 4, 'Black')
print(dog1)
print(dog2)
print(dog1 == dog2)

cat1 = Cat('Murzik', 8, 'Grey')
cat2 = Cat('Murzik', 8, 'Grey')
print(cat1)
print(cat2)
print(cat1 == cat2)

arr = np.arange(0, 20, 1)
print(arr)

arr = np.linspace(0, 20, 100)
print(arr)

arr = (100 - - 100) * np.random.random(100) - 100
print(arr)

print(np.cos(arr))

print(np.square(arr))

print(np.cos(arr) + np.square(arr))

print(np.cos(arr) / np.square(arr))

print(arr.min())

print(arr.std())

print(arr < 0)

np.insert(arr, 1, -2)

np.delete(arr, 1)

np.sort(arr)

print(np.sort(arr))

print(arr[arr > 0])

matrix = np.array(
    [
        (100 - - 100) * np.random.random(10) - 100,
        (100 - - 100) * np.random.random(10) - 100,
        (100 - - 100) * np.random.random(10) - 100
    ],
    dtype=np.int32
)

print(matrix)

print(matrix.shape)

print(matrix.reshape(5, 6))

matrix = np.random.random((2, 2))

print(matrix)

print(np.resize(matrix, (6, 6)))

print(np.zeros((4, 5)))

print(np.eye(4))

print(np.full((4, 5), 228))

print(np.eye(4) - np.random.random((4, 4)))

matrix = np.random.random((4, 6))

print(matrix)

print(np.delete(matrix, 1, axis=1))

print(matrix.max())

print(matrix.max(axis=0))

print(matrix)

print(matrix.T)

data = pn.Series(['Russian', 'English', 'Japanese'], index=['ru', 'en', 'jap'])

print(data)

print(data[['ru', 'jap']])

data['usa'] = 'American'

print(data)

print(data.drop(index=['en']))

print(data.max())

data = pn.DataFrame([[1, 4, 5], [2, 6, 5]], index=['x', 'y'], columns=['1', '2', '3'])

print(data)
