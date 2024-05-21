# Conectores logicos
#and
sueldo = 15000
antiguedad =11
if sueldo >= 15000 and antiguedad >=10:
    print('Verdadero')
else:
    print('Falso')

# or
opcion = int(input('Ingrese opcion: '))
if opcion == 1 or opcion==3 or opcion ==5:
    print('Verdadero')
else:
    print('Falso')
    
# not
edad = 22
if edad > 18:
    print('verdadero')
else:
    print('Falso')
    
if not edad < 18:
    print('Verdadero con not')
else:
    print('Falso con not')