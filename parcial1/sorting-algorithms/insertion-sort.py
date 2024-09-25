#! python3 
# insertion-sort.py - Insertion Sort

import random

def insertion_sort(arr):
    for j in range(1, len(arr)):
        key = arr[j]
        i = j - 1
        while i >= 0 and arr[i] > key:
            arr[i + 1] = arr[i]
            i -= 1
        arr[i + 1] = key

def random_list(size):
    return [random.randint(1, 100) for _ in range(size)]

numbers = random_list(10)

print(f"\nThe original list is:\t{str(numbers)}")
insertion_sort(numbers)

print(f"\nThe sorted list is:\t{str(numbers)}")
