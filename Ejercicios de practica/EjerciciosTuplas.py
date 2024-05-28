# Ejercicio 2:
# Crear y acceder a los elementos de una tupla:
# al tupla tiene que contener los numeros del 1
# al 5, imprimir el primer valor y el ultimo
'''
tupla =(1,2,3,4,5)
print(tupla[0], tupla[-1])
'''
# Ejercicio 3:
# Desempaquetar una tupla
# Crear una tupla con tres elementos
# Desempaquetar la tupla en tres variables e
# imprimir
'''
misDatos = ("Agostina",'Noriega',22)
nombre,apellido,edad = misDatos
print(nombre)
print(apellido)
print(nombre)
'''

# Ejercicio 4: Crear dos tuplas con los elementos
# que quieras , concátenalas en una nueva tupla
# repite la nueva tupla dos veces y almacenala
# en una nueva tupla
'''
tupla1 = ('a','b','c')
tupla2 = ('d','e','f')
tuplaC = tupla1+tupla2
tuplaM = tuplaC * 2
print(tuplaM)
'''
# Ejercicio 5:
# crear una tupla con los numeros del 1 al 10 e
# imprimir una sub-tupla que contenga del tercer
# al sexto elemento
'''
numeros = (1,2,3,4,5,6,7,8,9,10)
subNumeros = numeros[2:9]
print(subNumeros)
'''
# Ejercicio 6:
# crear una tupla con los numeros del 1 al 15 e
# imprimir una sub-tupla que contenga los numeros
# pares

'''
numeros = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15)
subNumeros = numeros[1:15:2]
print(subNumeros)
'''
# Ejercicio 7:
# Hacer que la tupla que se creo antes comience
# desde el 15 y termine en 1

numeros = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15)

subNumeros = numeros[::-1]
print(subNumeros)

#Ejercicio 8:
# Crear una variable con tu nombre y darlo vuelta
nombre="matias"
nomR = nombre[::-1]
print(nomR)
