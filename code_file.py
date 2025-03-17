import pandas as pd
import time

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

def main():
    df = load_dataset("diabetes.csv")
    column_to_search = input("Choose a column to search (Glucose, Age, BMI, etc.): ")
    value_to_search = float(input("Enter a value to search for: "))
    search_method = int(input("Choose search method:\n1. Linear Search\n2. Binary Search\nEnter choice: "))
    
    if search_method == 2:
        print(f"Sorting \"{column_to_search}\" column before Binary Search...")
        df = df.sort_values(by=[column_to_search]).reset_index(drop=True)
    
    values = df[column_to_search].tolist()
    index = linear_search(values, value_to_search) if search_method == 1 else binary_search(values, value_to_search)
    
    if index != -1:
        print(f"{['Linear', 'Binary'][search_method - 1]} Search: Found at row index {index}")
    else:
        print("Value not found.")
    
    column_to_sort = input("Choose a column to sort (Glucose, Age, BMI, etc.): ")
    sort_method = int(input("Choose sorting algorithm:\n1. Bubble Sort\n2. Selection Sort\n3. Insertion Sort\n4. Quick Sort\nEnter choice: "))
    
    sorting_algorithms = {1: bubble_sort, 2: selection_sort, 3: insertion_sort, 4: quick_sort}
    sorted_values = sorting_algorithms[sort_method](df[column_to_sort].tolist())
    df[column_to_sort] = sorted_values
    
    print(f"Sorting by \"{column_to_sort}\" using {['Bubble Sort', 'Selection Sort', 'Insertion Sort', 'Quick Sort'][sort_method - 1]}...")
    print("Sorting completed.")
    df.to_csv("sorted-diabetes.csv", index=False)
    print("Sorted data saved as \"sorted-diabetes.csv\".")

if __name__ == "__main__":
    main()
