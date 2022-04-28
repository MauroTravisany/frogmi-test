import unittest
import sys,os
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE)
import frogmi
import random
import time
import string
def str_time_prop(start, end, time_format, prop):

    stime = time.mktime(time.strptime(start, time_format))
    etime = time.mktime(time.strptime(end, time_format))

    ptime = stime + prop * (etime - stime)

    return time.strftime(time_format, time.localtime(ptime))

def random_date(start, end, prop):
    return str_time_prop(start, end, '%d-%m-%Y', prop)
    



class TestDates(unittest.TestCase):
    
    
    def setUp(self):
        print("Preparando el contexto")
        self.fecha_beggin, self.fecha_finish = "19-04-2022", "24-04-2022"
        self.date_random_beggin = random_date(self.fecha_beggin, self.fecha_finish, random.random())
        self.date_random_final = random_date(self.fecha_beggin, self.fecha_finish, random.random())
        self.other_variable =  random.choice(string.ascii_letters)+self.fecha_beggin
        print(" fecha 1 :%s,  fecha 2 %s"%(self.date_random_beggin, self.date_random_final) )
        print(" Fecha con mal formato: %s"%(self.other_variable))
        
    def test_date(self):
        print(f"\n////////////////////////////Test referente a fechas aleatorias entre un plazo definido //////////////////////////////////\n")
        print("Test : frogmi.Store(%s, %s)"% (self.date_random_beggin,self.date_random_final))
        self.store = frogmi.Store(self.date_random_beggin,self.date_random_final)
        if (self.date_random_beggin<=self.date_random_final ):
            self.assertEqual("Instancia creada correctamente", str(self.store))
        if(self.date_random_beggin>self.date_random_final):
            self.assertEqual("Las fechas que ingreso no estan dentro de los plazos registrados en el sistema.", str(self.store))
        print(f"\n////////////////////////////Test referente a una fecha ingresada con error de formato aleatoreo//////////////////////////////////\n")
        print("Test : frogmi.Store(%s, %s)"% (self.date_random_beggin,self.other_variable))
        self.store_bad = frogmi.Store(self.date_random_beggin,self.other_variable )
        self.assertEqual("El formato ingresado de fechas esta incorrecto, verifique que cada fecha corresponda a dd-mm-año", str(self.store_bad))
        
    def test_type_incidents(self):
        print(f"\n////////////////////////////Test de tipo de retorno en incident_status //////////////////////////////////\n")
        print("Test : store.incident_status()")
        self.store = frogmi.Store(self.date_random_beggin,self.date_random_final)
        self.store.incident_status()
        if (self.date_random_beggin<=self.date_random_final ):
            assert type(self.store.incident_status()) is dict
        if(self.date_random_beggin>self.date_random_final):
            self.assertEqual("No hay datos para las fechas ingresadas en la instancia o fueron mal ingresadas las fechas", str(self.store.incident_status()))
        print(f"\n////////////////////////////Test de error si fueron ingresadas mal las fechas//////////////////////////////////\n")
        print("Test : store.incident_status() con frogmi.Store(%s, %s) "% (self.date_random_beggin,self.other_variable))
        self.store_bad = frogmi.Store(self.date_random_beggin,self.other_variable)
        self.assertEqual("No hay datos para las fechas ingresadas en la instancia o fueron mal ingresadas las fechas", str(self.store_bad.incident_status()))
        
    
        
    def tearDown(self):
        print("Destruyendo el contexto")
        del(self.date_random_beggin)
        del(self.date_random_final)
        del(self.other_variable)




if __name__ == '__main__':
    unittest.main() 