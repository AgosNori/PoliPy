# While

# Contar del 1 al 5
'''
numero = 1 # inicializarlo con el valor de 1
while numero <= 5: # mientras numero sea menor o igual a 5
    print(numero)
    numero = numero + 1  # numero += 1
'''

# Ejercicio 2:
# crear una variable, inicializarla en 1
# y mostrar hasta 10
'''
numero = 1
while numero <= 10: # mientras numero sea menor o igual a 5
    print(numero)
    numero = numero + 1  # numero += 1
'''
# Ejercicio 33:
'''
var = 0
while var < 6:
    print(var)
    var += 1
'''
# Ejercicio 34
'''
numero = 1
while numero <= 10: # mientras numero sea menor o igual a 5
    print(numero)
    numero = numero + 1  # numero += 1
'''

# Ejercicio 35
'''
respuesta = input('Ingrese sí para inciar el proceso ?')
while respuesta == 'sí':
    respuesta = input('Desea continuar ?')
    
print('fin del proceso')
respuesta = input('Desea continuar ?')
while respuesta != 'sí':
    respuesta = input('Desea continuar ?')
    
print('fin del proceso')

'''

# Ejercicio 36
'''
contraseña = input('Ingrese la contra:')
contraseñaR = input('Ingrese nuevamente la contra:')
while contraseña != contraseñaR:
    print('Contraseña incorrecta')
    contraseña = input('Ingrese la contra:')
    contraseñaR = input('Ingrese nuevamente la contra:')
   
print('Contraseña correcta') '''
# Ejercicio 37
'''
sumatoria = 0
numeros = int(input('Imgrese un numero:'))

while numeros != 0:
    sumatoria += numeros
    numeros = int(input('Ingrese un numero:'))
print('La sumatoria total es: ',sumatoria)
''' 
# Ejercicio 38
'''
sumPositivos = 0
numeros = int(input('Imgrese un numero:'))

while numeros != 0:
    if numeros > 0:
        sumPositivos += numeros
    numeros = int(input('Ingrese un numero:'))
    
print('La sumatoria total  de los n positivos es: ',sumPositivos)
'''
# Ejercicio de practica
# Hacer la sumatoria de todos los numeros negativos
sumNegativos = 0
num = int(input('Imgrese un numero:'))
'''
while num != 0:
    if num >= 0 :
        print('Ingrese solo numeros negativos')
        sumNegativos += num
    num = int(input('Ingrese un numero:'))
    
print('La sumatoria total  de los n negativos es: ',sumNegativos)

sumatoria = 0
num = int(input('Imgrese un numero:'))

while num <= 0:
    if num > 0 :
        print('Ingrese solo negativos')
        sumatoria += num
    num = int(input('Ingrese un numero:'))
    
print('La sumatoria total  de los n negativos es: ',sumatoria)

'''
SumNegativos = 0
SumPositivos = 0
numE = int(input('Ingrese un numero: '))
while numE != 0:

    if numE >= 1:
        SumPositivos += numE
    else:
        SumNegativos += numE
    numE = int(input('Ingrese un numero: '))
print('La sumatoria de los positivos es: ',SumPositivos)
print('La sumatoria de los negativos es: ',SumNegativos)






    