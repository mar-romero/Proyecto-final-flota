
def distribucion ():
    import csv
    import datetime
    import time
    lis_cho = []
    csvfile = open('flota.csv', 'r+')
    with open('flota.csv') as fo:
        data = list(csv.DictReader(fo))
        no = open('distibucion.txt', "w")
        hoy = datetime.datetime.today()
        hora = ('{:%H:%M:%S}'.format(hoy))
        idcho = int(input('Ingrese ID del chofer:\n'))
        no_existe = True
        for i in range(len(data)):
            cho = data[i]
            chofer = int(cho.get('ID CHO'))
            nom_cho = str(cho.get('CHOFER'))
            if chofer == idcho:
                no_existe = False
                print("Buena distribucion")
                idcho_tx = str(idcho)
                no.write(nom_cho + "," + idcho_tx + ", , ," + hora + " \n")
                no.flush()
                break
        if no_existe:
            print("El ID no esta en la lista")
    csvfile.close()
    no.close()