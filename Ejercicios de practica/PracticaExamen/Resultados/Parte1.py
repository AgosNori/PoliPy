# Resultados parte 1
num = int(input('Ingrese un numero: '))
if num > 0:
    print('Es positivo')
elif num == 0:
    print('Es cero')
else:
    print('Es negativo')
    
# Resultado 2
num1= int(input('Ingrese el primer numero: '))
num2= int(input('Ingrese el segundo numero: '))
    
print('El mayor es: ',max(num1,num2))

# Resultado 3
año = int(input('Ingrese un año: '))
if (año % 4 ==0 and año %100 != 0 or año %400==0):
    print('año bisiesto')
else:
    print('año no bisiesto')
    
# Resultado 4
numero = int(input('Ingrese un numero :'))
if numero %2 == 0:
    print('Es par')
else:
    print('No es par')
    
# Resultado 5
edad = int(input('Ingrese su edad: '))
teorico =  input('Aprobo el examen teorico?:')
practico =  input('Aprobo el examen practico?:')
if edad >= 18 and teorico == 'si' and practico == 'si':
    print('Puede acceder a la licencia de conducir')
else:
    print('No puede acceder a la licencia de conducir')

# Resultado 6
lado1 = int(input('ingrese el lado 1 del triangulo :'))
lado2 = int(input('ingrese el lado 2 del triangulo :'))
lado3 = int(input('ingrese el lado 3 del triangulo :'))

if lado1 == lado2 ==lado3:
    print('Es equilatero')
elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
    print('Es isosceles')
else:
    print('Es escaleno')
    
# Resultado 7
letraIngresada = input('ingrese una letra:')
if letraIngresada in 'aeiouAEIOU':
    print('Es vocal')
else:
    print('Es consonante')
    
# Resultado 8
añoCualquiera = int(input('ingresa un año :'))
if añoCualquiera >= 2001 and añoCualquiera <= 2100:
    print('Es siglo xxi')
else:
    print('No es siglo xxi')
    
# Resultado 9
ang1 = float(input('ingrese el angulo 1: '))
ang2 = float(input('ingrese el angulo 2: '))
ang3 = float(input('ingrese el angulo 3: '))
if ang1 < 90 and ang2 < 90 and ang3 < 90:
    print( "El triángulo es agudo")
elif ang1 == 90 or ang2 == 90 or ang3 == 90:
    print( "El triángulo es rectángulo")
else:
    print( "El triángulo es obtuso")
    
# Resultado 10
nota1= float(input('Ingrese la nota 1: '))
nota2 = float(input('Ingrese la nota 2: '))
nota3 = float(input('Ingrese la nota 3: '))

promedio = (nota1+nota2+nota3)/3
if promedio > 7:
    print('Aprobo la materia')
else:
    print('No aprobo')
    
# Resultado 11
numerillos = (1,2)
print(numerillos[::-1])

# Resultado 12
numbers = (1,2,3,4,5)
suma = 0
for numerito in numbers :
    suma += numerito
print(suma)

# Resultado 13
tuplaNumeros = (1,2,353,54,244,775,78)
 
print( max(tuplaNumeros))

# Resultado 14
tupla1= (1,2,3,4,5)
tupla2= (6,7,8,9,10)
print(tupla1+tupla2)

# Resultado 15
tupla = ()
if tupla == ():
    print('vacia')
else:
    print('tiene datos')

# Resultado 16
tuplaInicial = (1,2,3,4,5,6,7,8,9,10)
tuplaFinal = ()
for valor in tuplaInicial:
    if valor % 2 == 0:
        tuplaFinal += (valor,)
print(tuplaFinal)

# Resultado 17
tuplaCadenas = ('Hola','Como','Andas','Wey')




