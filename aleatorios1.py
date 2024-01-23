import os
from random import randint, uniform

os.system('clear')

'''
randint -> genera números aleatorios enteros en un rango especificado por el desarrollador.
uniform -> genera números aleatorios flotantes o decimales en un rango especificado por el desarrollador.
'''

n1 = randint(-100,100)
n2 = uniform(1,50)

print(n1)
print(n2)

os.system('ls')