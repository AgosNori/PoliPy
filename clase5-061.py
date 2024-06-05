def mensaje():
    print('Hola Mundo')
    
    
mensaje()

### Ejercicios
# Crear una funcion que muestre por
# pantalla el nombre completo con la edad

def datos(nom,ape,edad):
    nomCompleto = nom + ' '+ ape
    print('Su nombre completo es: ',nomCompleto, 'y tiene: ',edad,'años')
    
# Darles los valores
datos('carlitos','perez',20)
# Pidiendo al usuario los datos
nombre = input('Ingrese su nombre: ')
apellido = input('Ingrese su apellido: ')
edad1 = int(input('Ingrese su edad: '))
datos(nombre, apellido, edad1)







