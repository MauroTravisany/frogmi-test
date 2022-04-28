# frogmi-test
Pequeño programa para demostrar mis habilidades técnicas

Este programa se puede diversificar en 4 ramas.

- Primero existe el programa principal frogmy.py que se encarga de cumplir la funcionalidad del sistema, obtener el diccionario con el estado de los incidentes.
- Segundo existe la carpeta resources, que en este caso tiene un archivo python llamado data.py que almacena unas variables con datos referente a los incidentes.
- Tercero existe la carpeta controler, la cual posee un programa capaz de manejar todos los datos del sistema, se encarga tanto de obtener, agregar, eliminar o filtrar datos.
- Cuarto existe la carpeta test, en esta carpeta se obtienen diversos test unitarios para corroborar que el sistema se este ejecutando correctamente.

/////////////////////////////////////////    Ejecución programa /////////////////////////////////////////

Para ejecutar el programa es necesario instanciar una variable y asignar la Clase "Store" a la vez indicar las fechas en las cuales se requiere solicitar información:

- Es importante recalcar que las fechas tienen que estar entre comillas y tener el formato "dd-mm-año" -

Cómo, por ejemplo:

    store = Store("19-04-2022", "21-04-2022")

- También es importante recalcar que se ingresa como primera fecha el inicio y segunda fecha el final del periodo a buscar.

Al ejecutar el comando existen 3 mensajes que puede llegar a obtener:
    - Instancia creada correctamente.
    - El formato ingresado de fechas esta incorrecto, verifique que cada fecha corresponda a dd-mm-año.
    - Las fechas que ingreso no están dentro de los plazos registrados en el sistema.

Para obtener la información solicitada referente a:

- The number of “open” cases between those dates.
- The number of “solved” cases between those dates.
- The average solution time between those dates (include only the solved cases).
- The current maximum solution time between those dates (include open cases using the current time).

Es necesario llamar al metodo incident_status(), de esta manera:

    store.incident_status()

Entregando como resultado un diccionario con las variables open_cases, solved_case, average_solution, maximum_solution:
 

    #{'open_cases': 0, 'solved_cases': 5, 'average_solution': 1.4, 'maximum_solution': 2.0}



/////////////////////////////////////////    Especificaciones de clases /////////////////////////////////////////

Profundizando más en la clase Store, es posible visualizar que contiene diferentes atributos:

    data_filtrada= []
    __empty:True
    mensaje: str()

data_filtrada corresponde a una Lista vacía, la cual lleva un papel importante debido a que se suministrará toda la información filtrada entre las dos fechas indicadas en la Clase "Store("19-04-2022", "21-04-2022")"
__empty, variable booleana cual va cambiando de estado mediante data_filtrada tenga datos o no.
mensaje, es una variable que retorna un mensaje, dependiendo del comportamiento del sistema.


Respecto a los métodos utilizados se pueden verificar 6 en la clase Store:
    
- __init__(self, dateinitial, datefinal )
- __str__(self)
- max_result(self)
- average_result(self)
- incident_status(self)
- transform_to_dt(list_return,data)

El metodo inicial __init__ recibe dos parámetros aparte de self, los cuales corresponden a la fecha inicial y de termino indicada por el usuario. Este método se encarga de llamar a un método de la clase controlador que se encarga de filtrar los datos retornando data_filtrada, las fechas mínimas de incidentes, la fechas máximas de incidentes y un mensaje.

El metodo __str__ recibe parámetro self y retorna un mensaje dependiendo del comportamiento del sistema, ya creada la instancia se puede realizar un print(store) y se visualizará un mensaje.

max_result(self) es un método el cual retorna el máximo resultado en tiempo que se ha demorado un incidente en ser resuelto. 

average_result(self) es un método el cual retorna el promedio en tiempo de todos los incidentes ya resueltos.

incident_status(self) ya se ha mencionado anteriormente su retorno, pero cabe destacar que utiliza los dos métodos anteriores -max_result y average_result- para obtener los resultados deseados.


transform_to_dt(data) es un método que es utilizado tanto para average_result y average_result, este método recibe una variable data, esta variable corresponde a una lista indicando el inicio y final de cada una de las 
incidencias; Este método convierte los string en objetos date y calcula las horas entre ambos días, registrándolo en la variable list_return.


Por otro lado, Existe la clase Controler ubicado en la carpeta controler/controler_data.py. Esta clase se caracteiza por el manejo de datos.

Los métodos que tiene la clase son los siguientes:

get_data_incidents: encargado de extraer todos los incidentes.

add_data_incidents: Agregar incidentes en memoria a la variable self.data
- variables de entrada: id de localidad, id de tienda, fecha de inicio, fecha de termino, hora de inicio, hora de termino, comentario
    - ejemplo : add_data_incidents(1,2,'19-04-2022','19-04-2022','solved','14:00','17:00',"lugar humedo" )

del_data_incident: Eliminar incidentes en memoria a la variable self.data
- variables de entrada: id de localidad, id de tienda, fecha de inicio, fecha de termino, hora de inicio, hora de termino
    - ejemplo : del_data_incident(1,2,'19-04-2022','19-04-2022','solved','14:00','16:00')

get_filtrado_incidents: Encargado de filtrar los incidentes entre un periodo de tiempo, retorna data_filtrada, las fechas mínimas de incidentes, la fechas máximas de incidentes y un mensaje.
- variables de entrada: fecha inicio y fecha final
    - get_filtrado_incidents("19-04-2022", "24-04-2022")

 /////////////////////////////////////////    TEST /////////////////////////////////////////

Para terminar, se ha creado un pequeño test el cual verifica si el sistema cumple integrando fechas al azar entre dos periodos de tiempo. Se puede verificar que manda error cuando el periodo está mal ingresado y que paso la prueba si están bien los tiempos indicados.

    - Para ejecutar el test es necesario correrlo mediante shell: python test.py


