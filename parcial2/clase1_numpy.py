#! python3

import numpy as np

lista = [1,2,3,4,5]
tupla = (1,2,3,4,5)
diccionario = {1: 'a', 2: 'b', 3: 'c'}
mi_set = {1, 2, 3, 4, 5}

iterables = [lista, tupla, diccionario, mi_set]

for i in iterables:
    print(np.array(i))