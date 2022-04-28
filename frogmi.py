"""CODING PROBLEM

Construct a simple Store class that has a collection of Incidents and an "incident_status" method.

An Incident is something that happens in the store that must be reported and solved, for example “the floor in the fruit area is dirty” and someone needs to clean it (this is the action needed to solve it). Also an Incident has an status that can be “open” if the incident has been reported but not solved or “solved” if the case has been solved.

The incident_status method of the Store class receives 2 dates and returns the following:
- The number of “open” cases between those dates.
- The number of “solved” cases between those dates.
- The average solution time between those dates (include only the solved cases).
- The current maximum solution time between those dates (include open cases using the current time).

Include automatic testing and documentation in a README file explaining how to use the classes, how to run the test and anything else you think is useful.

Upload your code to Github (or any Git repository you want) and send us the link where we can clone your repository.

An example for the execution of the method incident_status can be:

>> # some_store is an already initialized Store class with
>> # associated Incidents in different status
>> some_store.incident_status()
>> {'open_cases': 4,'closed_cases': 10, 'average_solution': 12, 'maximum_solution': 48}

You can use any programming language you want."""

from datetime import datetime
import controler.controler_data as controler_class

class Store():
        
    data_filtrada= []
    __empty:True
    mensaje: str()
    
    def __init__(self, dateinitial: 'datetime', datefinal: 'datetime')->'list':
        # La clase store parte inicializada con los datos filtrados entre fechas
        controler = controler_class.Controler()
        filtrado, date_min, date_max, msj = controler.get_filtrado_incidents(dateinitial,datefinal)
        if filtrado == []:
                self.__empty = True
                self.mensaje = "Las fechas que ingreso no estan dentro de los plazos registrados en el sistema."
                print(self.mensaje)
                print("El mínimo plazo corresponde a %s y el plazo máximo corresponde a %s" % (min(date_min),max(date_max)))
        elif filtrado == None:
            self.__empty = True
            self.mensaje = msj
            print(msj)
        else:
                self.__empty = False
                self.data_filtrada = filtrado
                self.mensaje ="Instancia creada correctamente"
                print(self.mensaje)
    
    def __str__(self): 
            return self.mensaje

    
    def max_result(self):
        # resultado maximo en un periodo de horas
        if self.__empty == False:  
            hours_begginfinal_total = list(map(lambda x:(x["date_beggin"]+" "+x["hour_beggin"], x["date_finish"]+" "+x["hour_finish"]), self.data_filtrada))
            list_hour_total =self.transform_to_dt(hours_begginfinal_total)
            maximum = max(list_hour_total)
            return(maximum)
        else:
            return None
    
    def average_result(self):
        # Promedio de un periodo de horas 
        if self.__empty == False:  
            hours_begginfinal_solved = list(filter(None,map(lambda x:(x["date_beggin"]+" "+x["hour_beggin"], x["date_finish"]+" "+x["hour_finish"])  if x["status"] == "solved" else None, self.data_filtrada)))
            list_hour_solved =self.transform_to_dt(hours_begginfinal_solved)
            average = sum(list_hour_solved)/len(list_hour_solved)
            return average
        else:
            return None
        
    def incident_status(self):
        # Retorna el estado de los incidentes 
        if self.__empty == False:  
            open_cases, solved_cases = sum([m["status"] == "open" for m in self.data_filtrada]), sum([m["status"] == "solved" for m in self.data_filtrada])
            status = {'open_cases': open_cases, 'solved_cases': solved_cases, 'average_solution': self.average_result(), 'maximum_solution': self.max_result()}
            print(status)
            return status
        else:
            return print("No hay datos para las fechas ingresadas en la instancia o fueron mal ingresadas las fechas")
        
    @staticmethod
    def transform_to_dt( data:'list' = []) -> 'list':
        #Resta un periodo de tiempo dia 2 - dia 1 retornando las cantidades de horas transcurridas
        list_return =[((( datetime.strptime(final,'%d-%m-%Y %H:%M')-datetime.strptime(beggin,'%d-%m-%Y %H:%M')).total_seconds())/3600) for beggin,final in data]
        return list_return
    
