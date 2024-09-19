import random

def exchange(arr,i,j):
    temp=arr[i]
    arr[i]=arr[j]
    arr[j]=temp

def partition(arr,p,r):
    x=arr[r]
    i=p-1
    for j in range(p,r):
        if arr[j]<=x:
            i=i+1
            exchange(arr,i,j)
    exchange(arr,i+1,r) 
    return i+1   

def quickSort(arr,p,r):
    if p<r:
        q=partition(arr,p,r)
        quickSort(arr,p,q-1)
        quickSort(arr,q+1,r)

def main():

    size = 100
    arr = [random.randint(1,100) for i in range(size)]
    print('Quicksort')
    print(f'Arreglo desordenado: {arr}')
    quickSort(arr,0,len(arr)-1)
    print(f'Arreglo ordenado {arr}')

if __name__ == '__main_':
    main()