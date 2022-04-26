import unittest
import sys,os
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE)
import frogmi
import random
import time
    
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
        print(" fecha 1 :%s,  fecha 2 %s"%(self.date_random_beggin, self.date_random_final) )

    def test_date(self):
        print("Realizando una prueba")
        self.store = frogmi.Store(self.date_random_beggin,self.date_random_final)
        self.assertEqual("Instancia creada correctamente", str(self.store))
        
        
    def tearDown(self):
        print("Destruyendo el contexto")
        del(self.date_random_beggin)
        del(self.date_random_final)


if __name__ == '__main__':
    unittest.main() 