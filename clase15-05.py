# Entradas
frente = int(input('Ingrese la medida del frente: '))
fondo = int(input('Ingrese la medida del fondo: '))
# Proceso y salida
perCuadrado = 4 * frente
perRectangulo = 2* frente + 2*fondo
supCuadrado = frente * fondo
supRectangulo = frente * fondo
if frente == fondo:
    print('Terreno cuadrado')
    print('El perimetro es: ',perCuadrado)
    print('La superficie es: ',supCuadrado)
elif frente != fondo:
    print('Terreno rectangular')
    print('El perimetro es: ',perRectangulo)
    print('La superficie es: ',supRectangulo)
     