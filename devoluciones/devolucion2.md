# Devolución 2
Fecha: 10-Julio-2020\
Autor: Hernán Contigiani

## Estructura de proyecto
Estuvimos revisando los cambios realizados respecto a la estructura del programa, en general están todo bien aplicados, quisieramos que renombres los archivos de python que poseen los nombres en mayúscula (Flota.py, Menu.py, etc) a minúscula (flota.py, menu.py).\
Esto es casi un requisito obligatorio de Python, ya que lo único que se invoca con mayúsculas en Python son las __clases__, ahora podrá no ser un problema pero lo sería en el corto plazo.

## Uso de funciones y bloques de código
Te pido disculpas sino me explique bien respecto al módulo horas, no era la idea que lo borrar sino todo lo contrario, que lo utilizaras. En el código estás repitiendo "acciones" copiando y pegando código lo cual debe reemplazarse por una función, es el uso más importante de funciones (construir bloques de código).\
Por ejemplo en el archivo __flota.py__ se encuentra el siguiente bloque de código:
```
hora_i = ('{:%H:%M:%S}'.format(hoy))
hora_sep = hora_i.split(":")
for u in range(3):
    hora_sep[u] = int(hora_sep[u])
hora_seg = hora_sep[0]*3600 + hora_sep[1]*60 + hora_sep[2]
hora_seg = int(hora_seg)
```
Luego tambíen se encuentra el siguiente bloque de código:
```
hora_cit_sep = hora_cit.split(":")
for u in range(3):
  hora_cit_sep[u] = int(hora_cit_sep[u])
hora_cit_seg = hora_cit_sep[0]*3600 + hora_cit_sep[1]*60 + hora_cit_sep[2]
hora_cit_seg = int(hora_cit_seg)
```
Ambos bloques de código son exactamente iguales, y este __método/bloque de código__ también se realiza en otros archivos. Lo que deseamos es que implementes una función que resuelva este bloque, ya que es uno de los uso fundamentales de funciones. Deseamos finalmente que tengas algo como lo siguiente:
```
def hora_a_segundos(hora_texto)
  '''Implementar función que pasa de hora en formato texto
  a hora en formato segundos en números (int)'''
  # Implementar funcion
  # hora_sep = ......
  # ....
  # ....
  # hora_seg = int(hora_seg)
  # al final usar "return" y retornar la hora en segundos
```
Luego en el código haras uso de esta función:
```
  hora_i = ('{:%H:%M:%S}'.format(hoy))
  hora_seg = hora_a_segundos(hora_i)
  
  # Lo mismo para todos los casos en donde se desee pasar de hora en formato texto
  # a hora en segundos en formato números.
```
