from cgi import test
from importlib.abc import ResourceLoader
import sys,os

from attr import dataclass
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE)

from resources.data import collection_incidents
from datetime import datetime

class Controler:
    
    def __init__(self) -> None:
        #Ejecuta el método get_data_incidents
        self.data = self.get_data_incidents()
    
    def get_data_incidents(self):
        #retorna el total de datos de incidentes
        self.data = collection_incidents
        return self.data
    
    def add_data_incidents(self,store_id,location_id,date_beggin,date_finish,status, hour_beggin,hour_finish, comment):
        #Método para almacenar en memoria mas incidentes
        try:
            date_beggin, date_finish = datetime.strptime(date_beggin, '%d-%m-%Y'), datetime.strptime(date_finish, '%d-%m-%Y')
            hour_beggin, hour_finish = datetime.strptime(hour_beggin, '%H:%M'),datetime.strptime(hour_finish, '%H:%M')
            self.data.append({"store_id":store_id , "location_id":location_id, "date_beggin":str(date_beggin.strftime('%d-%m-%Y')), "date_finish":str(date_finish.strftime('%d-%m-%Y')), "status": status, "hour_beggin": str(hour_beggin.strftime('%H:%M')), "hour_finish": str(hour_finish.strftime('%H:%M')), "comment":comment})
        except ValueError:
            print("Fechas invalidas, favor de revisar que las fechas esten en el formato correcto: dd-mm-yy")
    
    def del_data_incident(self, store_id, location_id, date_beggin,date_finish,status, hour_beggin,hour_finish ):
        #Metodo para eliminar incidentes en memoria 
        try:
            date_beggin, date_finish = datetime.strptime(date_beggin, '%d-%m-%Y'), datetime.strptime(date_finish, '%d-%m-%Y')
            hour_beggin, hour_finish = datetime.strptime(hour_beggin, '%H:%M'),datetime.strptime(hour_finish, '%H:%M')
            data_whitout_incident = [i for i in self.data if not (i['store_id'] == store_id and i['location_id'] == location_id and i['date_beggin']==str(date_beggin.strftime('%d-%m-%Y')) and i['date_finish']==str(date_finish.strftime('%d-%m-%Y')) and i['status']==status and i['hour_beggin']==str(hour_beggin.strftime('%H:%M')) and i['hour_finish']==str(hour_finish.strftime('%H:%M'))) ]
            self.data = data_whitout_incident
            return self.data
        except ValueError:
            print("Datos invalidos, favor de revisar que las fechas esten en el formato correcto: dd-mm-yy")
    
    def get_filtrado_incidents(self,dateinitial, datefinal):
        #metodo para filtrar incidentes en un periodo de tiempo y almacenarlo en un listado de diccionarios, obtener un listado de fechas mínimas, fechas máximas y un comentario 
        date_now = datetime.now()
        try:
            dateinitial, datefinal = datetime.strptime(dateinitial,'%d-%m-%Y'), datetime.strptime(datefinal,'%d-%m-%Y')
            date_min =set(x["date_beggin"] for x in self.data)
            self.data = [{**d, 'date_finish': d['date_finish'] if d['date_finish'] is not None else date_now.strftime('%d-%m-%Y')} for d in self.data]
            self.data = [{**d, 'hour_finish': d['hour_finish'] if d['hour_finish'] is not None else date_now.strftime('%H:%M')} for d in self.data]
            date_max =set(x["date_finish"] for x in self.data)
            filtrado = list(filter(lambda x: datetime.strptime(x['date_beggin'],'%d-%m-%Y')  >= dateinitial and datetime.strptime(x['date_finish'],'%d-%m-%Y') <= datefinal, self.data ))
            self.mensaje ="El formato de las fechas son correctas"
            return [filtrado, date_min, date_max, self.mensaje]
        except ValueError:
            self.mensaje ="El formato ingresado de fechas esta incorrecto, verifique que cada fecha corresponda a dd-mm-año"
            filtrado,date_min, date_max = None, None, None
            return [filtrado, date_min, date_max, self.mensaje]
