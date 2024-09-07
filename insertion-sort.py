#! python3 
# insertion-sort.py - 

def insertion_sort(arr):
    for j in range(1, len(arr)):
        key = arr[j]
        i = j - 1
        while i >= 0 and arr[i] > key:
            arr[i + 1] = arr[i]
            i -= 1
        arr[i + 1] = key

def generar_numeros_aleatorios(cantidad):
    return [random.randint(1, 100000) for _ in range(cantidad)]

numbers = [1,2,754,32,54,2,8,2,3,53,23,8,5,6]

insertion_sort(numbers)

print((numbers))