# Escriba un programa que simule una hucha. El programa solicitará primero una 
# cantidad, que será la cantidad de dinero que queremos ahorrar. A continuación,
# el programa solicitará una y otra vez las cantidades que se irán ahorrando, 
# hasta que el total ahorrado iguale o supere al objetivo. El programa no comprobará
# que las cantidades sean positivas.

sumatoriaDinero = 0
objetivo = float(input('Cual es tu objetivo para ahorrar?:'))
dineroIngresado = float (input('Cuanto van a ingresar?: '))

while dineroIngresado != objetivo:
    sumatoriaDinero += dineroIngresado
    if sumatoriaDinero >= objetivo:
        print('Cumpliste tu objtivo')
    else:
       dineroIngresado = float(input('Cuanto van a ingresar?: '))
      
print('Total ahorrado hasta el momento es: ',sumatoriaDinero)

