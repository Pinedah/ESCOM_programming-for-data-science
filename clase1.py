#! python
# clase1.py - Miercoles Septiembre 11, 2024

l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

x = 0
if x == 5:
    print("El valor es cinco desde aqui te brinco")
else:
    print("El valor NO es cinco desde aqui te brinco")

for element in l1:
    print(element, end=" ")
print('\n')

for i in range(0, 10, 2):
    print(l1[i], end=" ")
print('\n')

for i in range(len(l1) - 1, -1, -1):
    print(l1[i], end=" ")
print('\n')

for i in range(len(l1) - 1, -1, -2):
    print(l1[i], end=" ")
print('\n')

print(l1[::])

print(l1[::-1])

print(l1[-2::-2])

print(l1[2:9:3])
print(l1[-2::-3])

print(l1[-1::-4])

print(l1[-2:-7:-2])

for i in range(0, 7, 3):
    print(l1[i])
else: # se ejecuta al final del for
    print("Termino :)")