def menu():
    print('1) Ingreso')
    print('2) Salida a distribuir')
    print('3) Rendicion')
    print('4) Terminar Dia')
    while True:
        try:
            opcion = int(input('Ingrese el numero de la opcion deseada: '))
            if opcion == 1:
                print('Eligio: ', opcion, ') Ingreso', sep="")
                return opcion
                break
            elif opcion == 2:
                print('Eligio: ', opcion, ') Salida a distribuir', sep="")
                return opcion
                break
            elif opcion == 3:
                print('Eligio: ', opcion, ') Rendicion', sep="")
                return opcion
                break
            elif opcion == 4:
                print('Eligio: ', opcion, ') Terminar el dia', sep="")
                return opcion
                break
            else:
                print(opcion, 'no es una opcion')
        except ValueError:
            print('Ingreso una opcion invalida')
