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



stores=[
        {"id":1,"store":"Wallmart",},
        {"id":2,"store":"Easy",}]

stores_location = [
    {"location_id":1,"store_id": 1, "location": "gran avenida 42"},
    {"location_id":2,"store_id": 1, "location": "gran avenida 5"},
    {"location_id":3,"store_id": 2, "location": "el golf 433"},
    {"location_id":4,"store_id": 2, "location": "independencia 13"},
    ]

collection_incidents = [
    {"store_id": 1, "location_id":2, "date_beggin":"19-04-2022", "date_finish":"19-04-2022", "status": "solved", "hour_beggin": "14:00", "hour_finish": "16:00", "comment":"the floor in the fruit area is dirty"},
    {"store_id": 1, "location_id":2, "date_beggin":"19-04-2022", "date_finish":"19-04-2022", "status": "solved", "hour_beggin": "10:00", "hour_finish": "11:00", "comment":"the floor in the fruit area is dirty"},
    {"store_id": 1, "location_id":1, "date_beggin":"20-04-2022", "date_finish":"20-04-2022", "status": "solved", "hour_beggin": "10:00", "hour_finish": "11:00", "comment":"the floor in the fruit area is dirty"},
    {"store_id": 1, "location_id":1, "date_beggin":"20-04-2022", "date_finish":None, "status": "open", "hour_beggin": "14:00", "hour_finish": None, "comment":"the floor in the fruit area is dirty"},
    {"store_id": 2, "location_id":3, "date_beggin":"21-04-2022", "date_finish":"21-04-2022", "status": "solved", "hour_beggin": "14:00", "hour_finish": "16:00", "comment":"the floor in the fruit area is dirty"},
    {"store_id": 2, "location_id":3, "date_beggin":"21-04-2022", "date_finish":"21-04-2022", "status": "solved", "hour_beggin": "10:00", "hour_finish": "11:00", "comment":"the floor in the fruit area is dirty"},
    {"store_id": 2, "location_id":4, "date_beggin":"22-04-2022", "date_finish":"22-04-2022", "status": "solved", "hour_beggin": "14:00", "hour_finish": "16:00", "comment":"the floor in the fruit area is dirty"},
    {"store_id": 2, "location_id":4, "date_beggin":"22-04-2022", "date_finish":None, "status": "open", "hour_beggin": "10:00","hour_finish": None, "comment":"the floor in the fruit area is dirty"},

]

class Store():
        
    data_filtrada= []
     
    def __init__(self, dateinitial, datefinal):
        date_now = datetime.now()
        dateinitial, datefinal = datetime.strptime(dateinitial,'%d-%m-%Y'), datetime.strptime(datefinal,'%d-%m-%Y')
        for x in collection_incidents:
            if x["date_finish"] == None :
                x["date_finish"] = date_now.strftime('%d-%m-%Y')
                x["hour_finish"] = date_now.strftime('%H:%M')
        filtrado = list(filter(lambda x: datetime.strptime(x['date_beggin'],'%d-%m-%Y')  >= dateinitial and datetime.strptime(x['date_finish'],'%d-%m-%Y') <= datefinal, collection_incidents ))
        self.data_filtrada = filtrado

    def max_result(self):
        list_hour_total =[]  
        hours_begginfinal_total = list(map(lambda x:(x["date_beggin"]+" "+x["hour_beggin"], x["date_finish"]+" "+x["hour_finish"]), self.data_filtrada))
        self.transform_to_dt(list_hour_total,hours_begginfinal_total)
        maximum = max(list_hour_total)
        return(maximum)
    
    def average_result(self):
        list_hour_solved =[]
        hours_begginfinal_solved = list(filter(None,map(lambda x:(x["date_beggin"]+" "+x["hour_beggin"], x["date_finish"]+" "+x["hour_finish"])  if x["status"] == "solved" else None, self.data_filtrada)))
        self.transform_to_dt(list_hour_solved,hours_begginfinal_solved)
        average = sum(list_hour_solved)/len(list_hour_solved)
        return average
        
    def incident_status(self):
        open_cases, solved_cases = sum([m["status"] == "open" for m in self.data_filtrada]), sum([m["status"] == "solved" for m in self.data_filtrada])
        status = {'open_cases': open_cases, 'solved_cases': solved_cases, 'average_solution': self.average_result(), 'maximum_solution': self.max_result()}
        print(status)
        return status
    
    def transform_to_dt(self, list_return, data): 
        for beggin,final in data:
            beggin,final = datetime.strptime(beggin,'%d-%m-%Y %H:%M'), datetime.strptime(final,'%d-%m-%Y %H:%M')
            list_return.append(((final-beggin).total_seconds())/3600)
        return list_return
    
store = Store("18-04-2022", "23-04-2022")
store.incident_status()