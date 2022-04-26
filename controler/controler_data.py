from cgi import test
import sys,os
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE)

from resources.data import collection_incidents
from datetime import datetime

class Controler:
    
    def get_data(self):
        self.data = collection_incidents
        return self.data
    
    def add_data(self,store_id,location_id,date_beggin,date_finish,status, hour_beggin,hour_finish, comment):
        data = self.get_data()
        try:
            date_beggin, date_finish = datetime.strptime(date_beggin, '%d-%m-%Y'), datetime.strptime(date_finish, '%d-%m-%Y')
            hour_beggin, hour_finish = datetime.strptime(hour_beggin, '%H:%M')
            data.append({"store_id":store_id , "location_id":location_id, "date_beggin":date_beggin, "date_finish":date_finish, "status": status, "hour_beggin": hour_beggin, "hour_finish": hour_finish, "comment":comment})
        except ValueError:
            print("Fechas invalidas, favor de revisar que las fechas esten en el formato correcto: dd-mm-yy")
    
    def modify_data(self):
        pass
    
    def get_filtrado(self,dateinitial, datefinal):
        date_now = datetime.now()
        try:
            dateinitial, datefinal = datetime.strptime(dateinitial,'%d-%m-%Y'), datetime.strptime(datefinal,'%d-%m-%Y')
            date_min, date_max = set(), set()
            self.get_data()
            for x in self.data:
                date_min.add(x["date_beggin"])
                if x["date_finish"] == None :
                    x["date_finish"] = date_now.strftime('%d-%m-%Y')
                    x["hour_finish"] = date_now.strftime('%H:%M')
                date_max.add(x["date_finish"])
            filtrado = list(filter(lambda x: datetime.strptime(x['date_beggin'],'%d-%m-%Y')  >= dateinitial and datetime.strptime(x['date_finish'],'%d-%m-%Y') <= datefinal, self.data ))
            self.mensaje ="El formato de las fechas son correctas"
            return [filtrado, date_min, date_max, self.mensaje]
        except ValueError:
            self.mensaje ="El formato ingresado de fechas esta incorrecto, verifique que cada fecha corresponda a dd-mm-año"
            filtrado,date_min, date_max = None, None, None
            return [filtrado, date_min, date_max, self.mensaje]
