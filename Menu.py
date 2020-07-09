def menu():
    print('1) Ingreso')
    print('2) Salida a distribuir')
    print('3) Rendicion')
    print('4) Terminar Dia')
    while True:
        try:
            opcion = int(input('Ingrese el numero de la opcion deseada: '))
            if opcion == 1:
                print("-------------------")
                print('Eligio: ', opcion, ') Ingreso', sep="")
                print("-------------------")
                return opcion
                break
            elif opcion == 2:
                print("-------------------------------")
                print('Eligio: ', opcion, ') Salida a distribuir', sep="")
                print("-------------------------------")
                return opcion
                break
            elif opcion == 3:
                print("---------------------")
                print('Eligio: ', opcion, ') Rendicion', sep="")
                print("---------------------")
                return opcion
                break
            elif opcion == 4:
                print("---------------------------")
                print('Eligio: ', opcion, ') Terminar el dia', sep="")
                print("---------------------------")
                return opcion
                break
            else:
                print("******************")
                print(opcion, 'no es una opcion')
                print("******************")
        except ValueError:
            print("***************************")
            print('Ingreso una opcion invalida')
            print("***************************")
