# frogmi-test
Pequeño programa para demostrar mis habilidades tecnicas
CODING PROBLEM

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

You can use any programming language you want.
