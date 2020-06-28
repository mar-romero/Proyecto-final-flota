def distribucion ()
    import csv
    import datetime
    import time
    lis_cho = []
    csvfile = open('flota.csv', 'r+')
    with open('flota.csv') as fo:
        data = list(csv.DictReader(fo))
        no = open('rendicion.txt', "w")
        while True:
            try:
                hoy = datetime.datetime.today()
                hora = ('{:%H:%M:%S}'.format(hoy))
                idcho = int(input('Ingrese ID del chofer:\n'))
                no_existe = True
                for i in range(len(data)):
                    cho = data[i]
                    chofer = int(cho.get('ID CHO'))
                    if chofer == idcho:
                        no_existe = False
                        hora_cit_seg = int(hora_cit_seg)
                        hora_pasa = (hora_cit_seg-900)
                        print("Espero que haya tenido ua buena jornada.Hasta mañana")
                        idcho_tx = str(idcho)
                        no.write(nom_cho + "," + idcho_tx + "," + hora + "," + " \n")
                        no.flush()
                        break
                if no_existe:
                    print("El ID no esta en la lista")
            except ValueError:
                print('No ingreso ID correcto')
    csvfile.close()
    no.close()
