
import math as mt

def normal(x):
    return (1 / (4 * mt.sqrt(2 * mt.pi))) * mt.exp(-((x - 158) ** 2) / 32)

a = 142
b = 174
numTrapecios = 20
delta = (b-a)/numTrapecios
valor1 = 142 + delta

f0 = normal(a)
fn = normal(b)
sumatoria=0

num_pasos = int((b - a) / delta) - 1 

print('tabla de trapecios\n')
for i in range(num_pasos):
    print(valor1,'\t',normal(valor1),'\n')
    sumatoria=sumatoria + normal(valor1)
    valor1=valor1+delta


sumatoria = 2 * sumatoria
probaFinal = (delta/2)*(f0+sumatoria+fn)

print("La probabilidad final es: ",probaFinal)