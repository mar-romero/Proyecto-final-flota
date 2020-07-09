'''
Archivos [Python]
Flota
---------------------------
Autor: Romero Marcelo Ezequiel
Version: 1.1

Descripcion:
Programa creado para el ingreso y egreso de plata 
para control interno
'''

__author__ = "Romero Marcelo Ezequiel"
__email__ = "romero-ar@hotmail.com"
__version__ = "1.1"

import menu as el
import csv
import datetime
import time

def flota ():
    csvfile = open('flota.csv', 'r')
    no_r = open('rendicion.txt', "w")
    no_i = open('ingreso.txt', "w")
    no_d = open('distibucion.txt', "w")
    with open('flota.csv') as fo:
        data = list(csv.DictReader(fo))
        while True:
            try:
                op = el.menu()
                if op == 1:
                    hoy = datetime.datetime.today()
                    hora_i = ('{:%H:%M:%S}'.format(hoy))
                    hora_sep = hora_i.split(":")
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
                            for u in range(3):
                                hora_cit_sep[u] = int(hora_cit_sep[u])
                            hora_cit_seg = hora_cit_sep[0]*3600 + hora_cit_sep[1]*60 + hora_cit_sep[2]
                            hora_cit_seg = int(hora_cit_seg)
                            hora_pasa = (hora_cit_seg-900)
                            if hora_seg >= hora_pasa:
                                print("--------------------------")
                                print("Puede pasar, buena jornada")
                                print("--------------------------")
                                idcho_tx = str(idcho)
                                no_i.write(nom_cho + "," + idcho_tx + "," +hora_cit + "," + hora_i + "," + "\n")
                                no_i.flush()
                                break
                            else:
                                print("*****************")
                                print("No puede ingresar")
                                print("*****************")
                                break
                    if no_existe:
                        print("*************************")
                        print("El ID no esta en la lista")
                        print("*************************")
                elif op == 2 :
                    hoy = datetime.datetime.today()
                    hora_d = ('{:%H:%M:%S}'.format(hoy))
                    idcho = int(input('Ingrese ID del chofer:\n'))
                    no_existe = True
                    for i in range(len(data)):
                        cho = data[i]
                        chofer = int(cho.get('ID CHO'))
                        nom_cho = str(cho.get('CHOFER'))
                        if chofer == idcho:
                            no_existe = False
                            print("------------------")
                            print("Buena distribucion")
                            print("------------------")
                            idcho_tx = str(idcho)
                            no_d.write(nom_cho + "," + idcho_tx + ", , ," + hora_d +"\n")
                            no_d.flush()
                            break
                    if no_existe:
                        print("*************************")
                        print("El ID no esta en la lista")
                        print("*************************")
                elif op == 3 :
                    hoy = datetime.datetime.today()
                    hora_r = ('{:%H:%M:%S}'.format(hoy))
                    idcho = int(input('Ingrese ID del chofer:\n'))
                    no_existe = True
                    for i in range(len(data)):
                        cho = data[i]
                        chofer = int(cho.get('ID CHO'))
                        nom_cho = str(cho.get('CHOFER'))
                        if chofer == idcho:
                            no_existe = False
                            print("-----------------------------------------------------")
                            print("Espero que haya tenido ua buena jornada. Hasta mañana")
                            print("-----------------------------------------------------")
                            idcho_tx = str(idcho)
                            no_r.write(nom_cho + "," + idcho_tx + ", , , , " + hora_r +"\n")
                            no_r.flush()
                            break
                    if no_existe:
                        print("*************************")
                        print("El ID no esta en la lista")
                        print("*************************")
                elif op == 4:
                    no_r.close()
                    no_i.close()
                    no_d.close()
                    break 
            except ValueError:
                print("*********************")
                print('Ingreso ID incorrecto')
                print("*********************")

if __name__ == '__main__':
    flota()