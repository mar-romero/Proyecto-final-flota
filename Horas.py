def horas():
    import datetime
    import time
    hoy = datetime.datetime.today() 
    hora = ('{:%H:%M:%S}'.format(hoy))
    print(hora)
    hora = hora.split(":")
    for u in range(3):
        hora[u]= int(hora[u])
    hora_seg = hora[0]*3600 + hora[1]*60 + hora[2]
    hora_seg_2 = (hora_seg-900)
    hora_fin = time.strftime('%H:%M:%S', time.gmtime(hora_seg))
    hora_fin_2 = time.strftime('%H:%M:%S', time.gmtime(hora_seg_2))
    print(hora_seg)
    print(hora_seg_2)
    print(hora_fin)
    print(hora_fin_2)