'''
Scritp description:
Cree una función que genere el lanzamiento de dos datos (1-6)
y que muestre por pantalla el mensaje ganador cuando genere dados iguales,
de lo contrario el mensaje dira: sigue intentando-
'''

#Importar biblioteca para generar números aleatorios enteros.
from random import randint

#Función para lanzar y generar los valores de los dos lados.
def dices():
    dice1 = randint(1,6)
    dice2 = randint(1,6)

    return dice1, dice2

#Salidas
d = dices()
d1 = d[0]
d2 = d[1]

print("Dices:", d)
print("Dice 1:", d[0])
print("Dice 2:", d[1])


#print("Dice1:", dice1)
#print("Dice2:", dice2)

if d1==d2:
        print("Felicidades eres el Ganador")
else:
        print("sigue intentando")
