# Tuplas
# Secuencia INMUTABLE, lo que significa que no le podemos cambiar los valores
'''
# Tupla vacia
t = ()
print(t)

# Tupla con un solo valor
t1 = (1,)   # t1 = 1,
print(t1)

# Tupla con varios valores
t2 = (1,2,3,4)    # t2 = 1,2,3,4
print(t2)

# función tuple()
saludo = 'Hola Mundo'
print(tuple(t2))


# Función len()
tupla = (12,45,67,12,45,67,12,45,67,12,45,67,12,45,67)
print(len(tupla))


tupla2=12,15,23
print(tupla2[1])
x= tupla2[2]
print(x)'''


# Ejercicio 31
# Entradas
nombreAlum = input('Ingrese el nombre del alumno: ')
nombreProf = input('Ingrese el nombre del profesor: ')
promedio = float(input('Ingrese el promedio (CON DECIMALES):'))
# Forma 1
datos = nombreAlum,nombreProf,promedio
print('est.', datos[0] , 'prof.',datos[1], round(promedio))
# Forma 2
print('Forma 2')
datos2 = ('est.','prof.')
print(datos2[0], nombreAlum , datos2[1],nombreProf, round(promedio))


palabra= 'ingrese'
print(palabra[4])

# Ejercicio 1:
# Crear una tupla que contenga cinco elementos:
#una cadena, un numero entero, un numero flotante,
#un booleano y otra cadena.
# Acceder al tercer elemento de la tupla e imprimirlo

#len()        1     2   3   4     5            elementos
#misDatos = ('Agos',22,1.71,True,'Noriega')
#indice       0     1   2    3    4
#indices misDatos[]
#print(misDatos[2])
















