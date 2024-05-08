# Estructura condicional
# Estructura
#if expresión logica:
#....
#else:
#....
    
#Ejercicio 26
#Entradas
'''
n1=int(input('Ingrese n1 :'))
n2=int(input('Ingrese n2 :'))
#Procesos
if n1 > n2: # si n1 es mayor a n2
    #rama verdadera
    mayor= n1
    menor=n2
elif n1 == n2: # sino si
    print('ambos son iguales')
else: #sino 
    #rama falsa
    mayor = n2
    menor = n1
print(menor,mayor)
   '''
# ejercicio 27
# e
a= int(input('Ingrese a :'))
b= int(input('Ingrese b :'))
c= int(input('Ingrese c :'))
# p
suma= a+b+c
resultado1= suma /2
if suma > 10:
   print(resultado1)
else:
    resultado = suma **3
    print(resultado)











