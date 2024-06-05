# Proyecto 1: Calculadora
# Crear un programa en Py que realice operaciones matematicas
# (suma, resta,multiplicacion, division y modulo ) utilizando
# funciones. Cada función debe recibir dos números como parámetro
# y devolver el resultado de la operación correspondiente.
# PD: Los números los debe introducir el usuario

# Funciones
# función suma
def suma(n1,n2):
    suma = n1+n2
    print('El resultado de la suma es: ', suma)
def resta(n1,n2):
    resta = n1-n2
    print('El resultado de la resta es: ', resta)
def multiplicacion(n1,n2):
    multi = n1*n2
    print('El resultado de la multiplicacion es: ', multi)
def division(n1,n2):
    if n2 == 0:
        print('Error: no se puede dividir por cero')
    else:
        divi = n1/n2
        print('El resultado de la division es: ', divi)
def modulo(n1,n2):
    if n2 == 0:
        print('Error: no se puede dividir por cero')
    else:
        modulo= n1%n2
        print('El resultado del modulo es: ', modulo)
# Entradas
num1 = int(input('Ingrese el primer numero :'))
num2 = int(input('Ingrese el segundo numero: '))
# Salidas
suma(num1,num2)
resta(num1,num2)
multiplicacion(num1,num2)
division(num1,num2)
modulo(num1,num2)










