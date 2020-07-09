# Devolución 1
Fecha: 8-Julio-2020
Autor: Hernán Contigiani

## Funcionamiento general del programa
El programa en general está muy bien realizado, hace lo que tiene que hacer y se entienda. Fue acertado realizar archivos separados para cada tarea a realizar, fue más simple de seguir el programa.\
Hay algunos detalles sobre PEP8 y aprovechamiento de código que quisieramos que revises que nos parece importante ir acostumbrandonos para las siguientes etapas.\
Luego de corregir estos detalles volvemos a revisar el proyecto, como la ejecución del programa estás a un paso de finalizar este proyecto.

## Estructrua de proyecto
Estas devoluciones son cometarios generales respecto a la estructura del proyecto en general
- Los nombres de los archivos deberían empezar con minúscula, tal como recomienda PEP8.
- Por lo que se entiende el archivo principal "lanzador" es "flota.py", dicho archivo debería tener la siguiente sección en donde se lance el programa:
```
if __name__ == '__main__':
    # Código lanzador
```
- En el archivo "float.py" se importan archivos como "Eleccion" que fueron renombrados y no se encuetra más en el proyecto.

## Comentarios por archivo
#### flota.py
- Siendo este el archivo principal y "lanzador" de nuestro programa falta la estructura de "if __name__" como se detalló anteriormente. Esto facilitará en el futuro implementar el programa como un servicio o realizar ensayos.
- Hay archivos que fueron renombrados y no actualizados en el documento, por lo que al intentar lanzarlo el programa no funcionó, hubo que buscar los archivos renombrados y modificarlos.

#### ingreso.py
El funcionamiento del "ingreso.py" es correcto, hay algunos detalles de sintaxis y de estructura importates, como por ejemplo:
- El nombre del archivo está en mayúscula.
- Se realizan sentensias de "import" dentro de la función, las sentensias deben estar por fuera. Se definen primero los "import" y luego las funciones del archivo/módulo.
- El archivo "float.csv" se lo habre para lectura y escritura "r+" pero solo se lo usa para lectura "r".
- Hay un gran bloque de código que se encarga de transformar la hora en hora_segundos, el cual se repite dos veces su uso. Ese bloque de código debe estar implementado en una función. Vimos que existe el módulo "horas.py" pero no es invocado para realizar tal fin, la función "horas" debería recibir como parámetro la hora que se desea convertir a segundos y retornar "return hora_seg" para que el código que llama la función obtenga el valor para usar.

#### distribución.py
El funcionamiento del "distribución.py" es correcto, en general los comentarios son los mismos que los antes mencioandos:
- Nombre del archivo en minúscula.
- Módulos de import deben ir al comienzo del archivo y no dentro de las funciones.
- El uso del archivo CSV podría solo ser "r".

#### rendicion.py
El funcionamiento del "rendicion.py" es correcto, en general los comentarios son los mismos que los antes mencioandos:
- Nombre del archivo en minúscula.
- Módulos de import deben ir al comienzo del archivo y no dentro de las funciones.
- El uso del archivo CSV podría solo ser "r".


#### Comentarios
- Ya cambie todo lo mencionado e elimine el modulo horas.
- Un error que me di cuenta es que se volvia a reinscribir una vez ingresado a cada modulo (el txt creado solo quedaba grabado un chofer,el ultimo) no encontre otra solucion que poner todo el codigo en el mismo archivo y cerrar elos txt cuando se ingrese
la opcion 4.
- Se modifico el archivo readme.md