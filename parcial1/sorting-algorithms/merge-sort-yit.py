import random
import math

def merge(arr, start, middle, end):
    left = []
    right = []
    for i in range(start, middle + 1):
        left.append(arr[i])
    for j in range(middle + 1, end + 1):
        right.append(arr[j])

    # print(f"Left {left} - Right {right}")

    i = j = 0
    k = start
    while i < len(left) and j < len(right): 
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        elif right[j] < left[i]:
            arr[k] = right[j]
            j += 1
        k += 1 

    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1
    
    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1


def mergeSort(arr, start, end):
    if start < end:
        # print('MergeSort: ', arr[start:end+1])
        middle = math.trunc((start + end) / 2)

        mergeSort(arr, start, middle)
        mergeSort(arr, middle + 1, end)
        merge(arr, start, middle, end)
    #else:
        #print(f'Base: {arr}')

def main():
    
    arr_size = 100000
    arr_start = 0
    arr = [random.randint(1, 100) for i in range(arr_size)]
    
    # print('\nMergeSort')
    # print(arr)

    mergeSort(arr, arr_start, len(arr) - 1)  # Aquí corriges el primer argumento

    print(f"\nOrdenao: ")
    #print(arr)

if __name__ == '__main__':
    main()