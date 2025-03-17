import csv
import time

def load_data():
    with open("diabetes.csv", newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        data = list(reader)
        return data

def valid_column(data, column):
    column = column.strip().lower()
    return next((key for key in data[0].keys() if key.lower() == column), None)

def linear_search(data, column, value):
    for index, row in enumerate(data):
        if float(row[column]) == value:
            return index
    return -1

def binary_search(data, column, value):
    sorted_data = sorted(data, key=lambda x: float(x[column]))
    left, right = 0, len(sorted_data) - 1
    while left <= right:
        mid = (left + right) // 2
        if float(sorted_data[mid][column]) == value:
            return mid
        elif float(sorted_data[mid][column]) < value:
            left = mid + 1
        else:
            right = mid - 1
    return -1
