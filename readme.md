### Proyecto final python inicial


*Este proyecto se encarga de controlar los horarios de una flota de una planta distribuidora(ingreso a la planta, egreso de distibucioion y rendicion al finalizar el dia),
lo choferes se registran por un unico ID y gracias a el se guardan los horarios*

Pre-requisitos 📋

El programa a utilizar seria visual studio code y el lenguaje de programacion Python.

#### Cuenta con 4 opciones⚙️
* Menu:
   
   * En este modulo te doy a elegir en que proceso se encuentra el vehiculo (ingreso, distribucion o rendicion) o si queres terminar el dia.

* Ingreso:

   * Se ingresa opcion 1 en el menu y se le pide el ID al chofer.
   * En esta opcion se compara la hora que fue citado el vehiculo con la hora en la que se presenta a la planta y solo puede ingresar si se presenta con 15 min de anticipacion, si
   es asi se graba en un archivo txt la hora de citacion y la hora de llegada a la planta, si llego antes de los 15 min permitidos para poder pasar a la planta no puede ingresar 
   y no se graba la hora que llego a la planta. Esto se logra gracias al ID con el que se identifica al chofer.
  
* Distribucion:

  * Se ingresa la opcion 2 en el menu y se le pide el ID al chofer.
  * En estaopcion solo se le agrega la hora en tiempo real que se fue de la planta y se graba en un archivo txt con su recpectivo nombre  e ID
  
* Rendicion:
  
  * Se ingresa la opcion 3 en el memnu y se le pide el ID al chofer.
  * En esta opcion solo se agrega la ora en tiempo real que vuelve a reingresar a la planta y se guarda en un archivo txt con su respectivo nombre e ID
  
   
 #### Notas📄
 
Al ingresar un opcion que no se encuentre en el menu, por consola se imprime: " (numero ingresado) no es una opcion" y vuelve a pedirte una opcion. Si se ingrese caracteres o letras
por consola se imprime "Ingreso una opcion invalida".

En ingreso, distribucion y rendicion es exactamente igual, al ingresar un ID incorrecto o letras, por consola se imprime "El ID no esta en la lista" y vuelve a la opcion del menu.

Esta separado con comas los archivos txt porque al finalizar el dia se puede pasar a un archivo excel y con la opciones de excel(solapa: datos, texto en columnas y poner la opcion cada coma es una columna) cada horario (ingres, distribucion, rendicion) se ponen en una columna diferente y poder tener todo mas facil en un archivo excel.


Construido con 🛠️
  * Python
  * Modulo CSV
  * Modulo datetime
  * Modulo time
  
  
  
  
Autor🖥️
  
### Romero Marcelo Ezequiel
 
