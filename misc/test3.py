import numpy as np


arr = np.array([[1, 1], [2, 2], [3, 3], [4, 4]])
probs = [.25, .25, .25, .25]
indicies = np.random.choice(len(arr), 1, p=probs)

array = (arr[indicies])
list = (array.tolist())
goal = [item for sublist in list for item in sublist]

print(goal)

arr5 = '1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 32, 33, 34, 35, 36, 37, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 53, 54, 55, 56, 57, 58, 59, 61, 62, 63, 64, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100'
number = len(arr5.split(','))
print(number)