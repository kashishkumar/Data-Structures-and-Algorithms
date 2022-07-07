# insertion sort
array = [31, 42, 59, 26, 41, 58]


def insertion_sort(array):
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        print("key: ", i)
        print("Subarray: ", array[0 : i - 1])
        while j >= 0 and array[j] > key:
            array[j + 1] = array[j]
            j = j - 1
        array[j + 1] = key
    return array


insertion_sort(array)


def insertion_sort_decreassing(array):
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        print("key: ", i)
        print("Subarray: ", array[0 : i - 1])
        while j >= 0 and array[j] < key:
            array[j + 1] = array[j]
            j = j - 1
        array[j + 1] = key
    return array


insertion_sort_decreassing(array)

# Linear search : input as array and a value x,
# output i such that x = A[i] or Nil if x not present


def linear_search(array, number):
    for i in range(len(array)):
        if array[i] == number:
            return i
    return "Not found"


linear_search(array, 59)


def swap(array, i, j):
    array[i], array[j] = array[j], array[i]
    return array


swap(array, 1, 2)


def insert(array, key):
    for index in reversed(range(key)):
        if array[index] > array[index + 1]:
            array = swap(array, index, index + 1)
        else:
            break
    return array


insert(array, 4)


def insertion_sort_modified(array):
    for key in range(1, len(array)):
        array = insert(array, key)

    return array


insertion_sort_modified(array)


array.sort()
array

spam = [1, 2, 3, 4]
spam2 = spam  # Shallow copy
spam2

spam2 = spam[:]

spam[3] = 100

spam2.index(100)


spam = {"color": "red", "age": 42, "eggs": 4}
(spam)

for key, value in spam.items():
    print(key, value)

"color" in spam
spam.get("age")

spam.setdefault("eggs", 2)

dic1 = {"a": 8, "d": 5, "c": 9, "d": 4}
dic2 = {"a": 4, "d": 5, "c": 6}
dic3 = {**dic1, **dic2}
dic3 == dic2

for i, value in enumerate(set(dic1.values())):
    print(value)


def count_ways_to_matrix_traverse(rows, columns):
    # Use dynamic programming
    # dp[i][j] = dp[i-1][j] + dp[i][j-1]
    dp = [[0 for i in range(columns)] for j in range(rows)]
    for i in range(rows):
        for j in range(columns):
            if i == 0 or j == 0:
                dp[i][j] = 1
            else:
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
    return dp[rows - 1][columns - 1]


array = [40, 10, 30, 20, 50]
def bubble_sort(array):
    for i in range(len(array)):
        for k in range(i):
            if array[k] > array[k+1]:
                array[k], array[k+1] = array[k+1], array[k]
    return array           
bubble_sort(array)