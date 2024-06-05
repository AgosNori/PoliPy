## Ejercicios de practica FOR
'''nombres = ("Agostina","Celeste","Mariela","Micaela")
for nom in nombres:
    print(nom)'''
# 1- Imprimir numeros del 1 al 10
'''
for num in range (1,11):
    print(num)
'''
# 2- Imprimir los elementos de una tupla que contenga frutas
'''
frutas = ("pera","manzana","naranja")
for caracter in frutas:
    print(caracter)
'''

# 3- Sumar numeros de una tupla
'''
numeros = 1,2,3,4,5
sumatoria = 0
for num in numeros:
    sumatoria += num
print('El resultado de la suma es: ',sumatoria)
'''

# 4- Imprimir los caracteres de una cadena
''''
nombre = "Agos"
for caracter in nombre:
    print(caracter)
'''
# 5- Imprimir numeros pares del 1 al 20
'''
for num in range(1,21):
    if num % 2 == 0:
        print(num)
'''
# 6- Imprimir los primeros 10 numeros elevados al cuadrado
#pow (variable,exponente) **
'''
for num in range(1,11):
    print(num**2)
'''

# 7- Contar vocales en una cadena
'''
nombreMascota = "CAPITAN"
vocales = "aeiouAEIOU"
contador = 0

for caracter in nombreMascota :
    if caracter in vocales:
        contador = contador + 1  # contador += 1
print('La cantidad de vocales es: ',contador)
'''
# 8- Multiplicacion de los primeros 5 numeros
'''
multi = 1
for num in range(1,11):
    if num <=5:
        multi *= num
print('El resultado de la multiplicacion es: ',multi)
'''


# 9- Vamos a crear las tablas de multiplicar (la del 5)
'''
for num in range(1,11):
    print(' 5 x ', num ,'=', num*5)
'''

# 10- Contar la cantidad de elementos de una tupla
'''
edades = ('12','12','12','12','12','12')
sumatoria = 0
for cant in edades:
    sumatoria +=1
print('La cantidad de elementos es: ',sumatoria)

'''

# 11- Imprimir los numeros impares del 1 al 20
'''
for num in range(1,21):
    if num % 2 != 0:
        print(num)
'''
# 12- Encontrar el numero más grande de una tupla
'''
numeros = 1,2,3,4,5,6,7,32,66,111,24467,22,2,2,2,2,2,2,
mayor = 0
for num in numeros:
    if num > mayor :
        mayor = num
print(mayor)
'''       
# 13- Contar la cantidad de letras que hay en una palabra



'''
nombre='antonela'
suma=0
for i in nombre:
    suma+=1
print(f'La cantidad de letras es {suma}')
'''

# 14- Escribe un programa que calcule la suma de todos los numeros
# del 1 al 10 e imprimir el resultado
'''
sumatoria = 0

for num in range(1,11):
    sumatoria += num

print("La suma de todos los números entre el 1 y el 10 es igual a",sumatoria)
'''
# 15- Cargar una tupla con 5 herramientas y luego imprimir
# 16- Escribe un programa que cuente y muestre la cant de vocales
# que hay en una palabra dada por el usuario
# 17- Imprimir numeros entre el 5 y el 20, saltando de tres en
# tres
# 18- Escribe un programa que imprima un patron de asteriscos
# en forma de triangulo. Debe tener una base y una altura de 5
# lineas. Cada linea del triangulo debe contener un numero+
# creciente de asteriscos, comenzando con 1 en la primera linea
# 2 asteriscos en la segunda y asi sucesivamente , hasta llegar
# a 5 asteriscos en la ultima linea. DEBE VERSE ASI:
'''
*
**
***
****
*****
'''
# 19- Contar cuantos numeros son mayores a cero
# 20- Requerir al usuario ue ingrese un numero positivo e
# imprimir todos los numeros correlativos entre el ingresado
# por el usuario y uno menos del doble del mismo.

