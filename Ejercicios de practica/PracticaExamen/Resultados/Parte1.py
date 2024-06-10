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