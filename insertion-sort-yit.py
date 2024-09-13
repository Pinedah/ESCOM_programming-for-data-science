import random
'''randint genera un numero aleatorio en un rango
    x=[random.randint(1,100) for i in range(10)]
    permit


'''
def insertionSort(A):
    #pass return para no hacer nada
    for j in range(1,len(A)):
        key = A[j]
        i=j-1
        while i>=0 and A[i]>key:
            A[i+1]=A[i]
            i=i-1
        A[i+1]=key

def miMain():
    #insertionSort()
    print('Mi maaaaaaiiinnnnn')
    listaDesordenada=[random.randint(100,5) for i in range(100000)]
    print(listaDesordenada)
    insertionSort(listaDesordenada)
    print(listaDesordenada)


if __name__ == '__main__':
    miMain()