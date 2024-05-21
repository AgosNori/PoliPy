# Ejercicios de practica - CONECTORES
# Ejercicio 1: Escribe un programa que solicite al usuario
# dos numeros enteros y determine si ambos numeros son
# mayores a 10
'''
num1= int(input('Ingrese el primer numero: '))
num2= int(input('Ingrese el segundo numero: '))

if num1 > 10 and num2 > 10:
    print('Son mayores')
else:
    print('No lo son')
'''
# Ejercicio 2: Escribe un programa que solicite al usuario
# dos numeros enteros y determine si al menos uno de ellos
# es par
# num1 % 2 == 0 ( se calcula si es par)
'''
num3= int(input('Ingrese el primer numero: '))
num4= int(input('Ingrese el segundo numero: '))

if num3 %2 ==  0 or num4 %2 == 0:
    print('Al menos uno es par')
else:
    print('Ninguno es par')
  '''  
# Ejercicio 3:
# Escribe un programa que solicite al usuario un numero
# entero y determine si el numero NO esta dentro de 1 y
# 100 (inclusive)
# utilizar el NOT
'''
if edad > 18:
    print('mayor')
    
if not edad < 18:
   print('mayor')
'''
'''

num5= int(input('Ingrese el primer numero: '))

if not 1 <= num5 <= 100:
    print('No  Esta entre 1 y 100')
else:
    print('Si esta entre 1 y 100')
    
  '''  
    
# Ejercicio 4: Escribe un programa que solicite al usuario
# un numero entero y determine si el numero es multiplo de 3
# 3 y multiplo de 5
'''
num = int(input('ingrese un numero: '))
if num %3 == 0 and num %5 == 0:
    print('Es multiplo de 3 y 5')
else:
    print('No lo es')
'''

# Ejercicio 5: Escribe un programa que solicite al usuario
# su nombre y determine si su nombre empieza con una vocal
# (A,E,I,O,U)
'''
nombre = input('Ingrese su nombre: ')
primraLetra= nombre[0]
if primraLetra.upper() == 'A' or primraLetra.upper() == 'E' or primraLetra.upper() == 'I' or primraLetra.upper() == 'O' or primraLetra.upper() == 'u':
    print('vocal')
else:
    print(' no vocal')
'''
# Ejercicio 6: Escribe un programa que solicite al usuario
# tres numeros enteros y determine si al menos uno de ellos
# es positivo
''' 
a = int(input('ingrese un numero: '))
b = int(input('ingrese otro numero: '))
c = int(input('ingrese el ultimo numero: '))

if a >= 0 or b >= 0 or c >=0:
    print('Hay un numero positivo')
else:
    print('Todos son negativos')
  '''  
#Ejercicio 7: Escribe un programa que solicite al usuario
#dos numeros enteros y determine si la suma de ambos es par
'''

num1 = int(input('Ingresar num1:'))
num2 = int(input('Ingresar num2:'))
suma = num1+num2

if suma % 2== 0:
    print('Es par')
else:
    print('No lo es')
'''
# Ejercicio 8: escribe un programa que solicite al usuario
# su edad y determine si tiene al menos 18 años y menos de
# 70 , y por lo tanto, esta en el rango para poder conducir
'''
edad = int(input('Ingrese su edad:'))
if edad >=18 and edad <=70:
    print('Puede manejar')
else:
    print('No puede')
'''

# Ejericio 9:Escribe un programa que solicite al usuario
# un año y determine si es bisiesto.
# Dato: un año es bisiesto si es divisible por 4, pero no
# por 100, a menos que tambien sea divisible por 400
'''
año = int(input('ingrese el año'))
if año % 4 == 0 and año % 100 != 0 or año % 400 == 0:
    print('año bisiesto')
else:
    print('No es bisiesto')
'''

# Ejercicio 10: Escribe un programa que solicite al usuario
# una palabra y determine si la palabra comienza y termina
# con la misma letra
palabra = 'sandias'
primeraL= palabra[0]
#ultimaL= palabra[len(palabra)-1]
ultimaL= palabra[-1]

if primeraL == ultimaL:
    print('Son iguales')
else:
    print('No lo son')






