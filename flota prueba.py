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

import csv
import datetime
import time

csvfile = open('flota.csv', 'r+')
import csv
import datetime
import time

with open('flota.csv') as fo:
    data = list(csv.DictReader(fo))
    hoy = datetime.datetime.today() 
    hora = ('{:%H:%M:%S}'.format(hoy))
    hora = hora.split(":")
    for u in range(3):
        hora[u]= int(hora[u])
    hora_seg = hora[0]*3600 + hora[1]*60 + hora[2]
    idcho = int(input('Ingrese ID del chofer:\n'))
    for i in range(len(data)):
        cho = data[i]
        chofer = int(cho.get('ID CHO'))
        hora_cit = str(cho.get('HORA DE CITACION'))
        hora_cit = hora_cit.split(":")
        for u in range(3):
            hora_cit[u]= int(hora_cit[u])
        hora_cit_seg = hora_cit[0]*3600 + hora_cit[1]*60 + hora_cit[2]
        if chofer == idcho:
            hora_pasar = (hora_cit_seg-900)
            if hora_seg >= hora_pasar:
                print("Puede pasar, Buena Jornada")
                hora_fin = time.strftime('%H:%M:%S', time.gmtime(hora_seg))
                #no puedo grabar en la columna inicio de carga
                writer.writerow({'inicio carga': hora_fin})
            else:
                print("No puede ingresar")
csvfile.close()