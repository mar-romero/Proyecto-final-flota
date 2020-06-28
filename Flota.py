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

import Eleccion as el
import Ingreso as ing
import distribucion as distr
import Reingreso as re
while True:
    try:
        op = el.menu()
        if op == 1:
           ing.ingreso()
        elif op == 2 :
            distr.distribucion()
        elif op == 3 :
            re.reingreso()
        elif op == 4:
            break 
    except ValueError:
        print('Ingreso ID incorrecto')