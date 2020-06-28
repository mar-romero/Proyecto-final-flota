def ingreso():
    import csv
    import datetime
    import time
    lis_cho = []
    csvfile = open('flota.csv', 'r+')
    with open('flota.csv') as fo:
        data = list(csv.DictReader(fo))
        no = open('ingreso.txt', "w")
        hoy = datetime.datetime.today()
        hora = ('{:%H:%M:%S}'.format(hoy))
        hora_sep = hora.split(":")
        for u in range(3):
            hora_sep[u] = int(hora_sep[u])
        hora_seg = hora_sep[0]*3600 + hora_sep[1]*60 + hora_sep[2]
        hora_seg = int(hora_seg)
        idcho = int(input('Ingrese ID del chofer:\n'))
        no_existe = True
        for i in range(len(data)):
            cho = data[i]
            chofer = int(cho.get('ID CHO'))
            if chofer == idcho:
                no_existe = False
                hora_cit = str(cho.get('HORA DE CITACION'))
                nom_cho = str(cho.get('CHOFER'))
                hora_cit_sep = hora_cit.split(":")
                lis_cho.append(chofer)
                for u in range(3):
                    hora_cit_sep[u] = int(hora_cit_sep[u])
                hora_cit_seg = hora_cit_sep[0]*3600 + hora_cit_sep[1]*60 + hora_cit_sep[2]
                hora_cit_seg = int(hora_cit_seg)
                hora_pasa = (hora_cit_seg-900)
                if hora_seg >= hora_pasa:
                    print("Puede pasar, buena jornada")
                    idcho_tx = str(idcho)
                    no.write(nom_cho + "," + idcho_tx + "," +hora_cit + "," + hora + "," + " \n")
                    no.flush()
                    break
                else:
                    print("No puede ingresar")
                    break
        if no_existe:
            print("El ID no esta en la lista")
    csvfile.close()
    no.close()