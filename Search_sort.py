import pandas as pd
import time

# LOAD DATA
def load_dataset(filename):
    return pd.read_csv(filename)

# LINEAR SEARCH - UNSORTED LIST
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

# LINEAR SEARCH - SORTED LIST
def sorted_linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
        elif arr[i] > target:
            return -1
    return -1

# BINARY SEARCH - SORTED LIST
def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (high + low) // 2
        if arr[mid] == target:
            return mid
        elif target < arr[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return -1

# BUBBLE SORT
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# SELECTION SORT
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

# INSERTION SORT
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# QUICK SORT
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

# EXECUTION TIME
def execution_start():
    start = time.time()
    return start

def execution_stop():
    stop = time.time()
    return stop

def execution_time(start, end):
    print(f"Time Taken: {end-start:.4f}s")


# MAIN

df = load_dataset("diabetes.csv")

while True:
    column_search = input("Choose a column to search (Glucose, Age, BMI, etc.): ").lower()
    if column_search == "glucose":
        column_search = "Glucose"
        break
    elif column_search == "age":
        column_search = "Age"
        break
    elif column_search == "bmi":
        column_search = "BMI"
        break
    elif column_search == "pregnancies":
        column_search = "Pregnancies"
        break
    elif column_search == "blood pressure":
        column_search = "BloodPressure"
        break
    elif column_search == "skin thickness":
        column_search = "SkinThickness"
        break
    elif column_search == "insulin":
        column_search = "Insulin"
        break
    elif column_search == "diabetes pedigree function":
        column_search = "DiabetesPedigreeFunction"
        break
    elif column_search == "outcome":
        column_search = "Outcome"
        break
    else:
        print("Please input proper column.")

while True:
    try:
        value_search = float(input("Enter a value to search for: "))
        if value_search is str:
            raise Exception
        else:
            break
    except Exception:
        print("Please input a number.")

while True:
    search_method = int(input("Choose search method:\n1. Linear Search\n2. Binary Search\nEnter choice: "))
    if search_method not in [1,2]:
        print("Please input search method.")
    else:
        break

timestart = execution_start()
if search_method == 2:
    print(f"Sorting \"{column_search}\" column before Binary Search...")
    df = df.sort_values(by=[column_search]).reset_index(drop=True)

values = df[column_search].tolist()
index = linear_search(values, value_search) if search_method == 1 else binary_search(values, value_search)

if index != -1:
    print(f"{['Linear', 'Binary'][search_method - 1]} Search: Found at row index {index}")
    timeend = execution_stop()
    execution_time(timestart,timeend)
else:
    print("Value not found.")
    timeend = execution_stop()
    execution_time(timestart,timeend)

while True:
    column_sort = input("Choose a column to search (Glucose, Age, BMI, etc.): ").lower()
    if column_sort == "glucose":
        column_sort = "Glucose"
        break
    elif column_sort == "age":
        column_sort = "Age"
        break
    elif column_sort == "bmi":
        column_sort = "BMI"
        break
    elif column_sort == "pregnancies":
        column_sort = "Pregnancies"
        break
    elif column_sort == "blood pressure":
        column_sort = "BloodPressure"
        break
    elif column_sort == "skin thickness":
        column_sort = "SkinThickness"
        break
    elif column_sort == "insulin":
        column_sort = "Insulin"
        break
    elif column_sort == "diabetes pedigree function":
        column_sort = "DiabetesPedigreeFunction"
        break
    elif column_sort == "outcome":
        column_sort = "Outcome"
        break
    else:
        print("Please input proper column.")

while True:
    sort_method = int(input("Choose sorting algorithm:\n1. Bubble Sort\n2. Selection Sort\n3. Insertion Sort\n4. Quick Sort\nEnter choice: "))

    sorting_algorithms = {1: bubble_sort, 2: selection_sort, 3: insertion_sort, 4: quick_sort}
    if sort_method not in sorting_algorithms.keys():
        print("Please choose a sorting method.")
    else:
        break
timestart = execution_start()
sorted_values = sorting_algorithms[sort_method](df[column_sort].tolist())
df[column_sort] = sorted_values

print(f"Sorting by \"{column_sort}\" using {['Bubble Sort', 'Selection Sort', 'Insertion Sort', 'Quick Sort'][sort_method - 1]}...")
print("Sorting completed.")
df.to_csv("sorted-diabetes.csv", index=False)
timeend = execution_stop()
print("Sorted data saved as \"sorted-diabetes.csv\".")
execution_time(timestart,timeend)



