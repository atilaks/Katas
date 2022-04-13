import random


class Department:

    def __init__(self):
        self._department = ["departmentA", "departmentB"]
        self.available_department = False

    def set_department_availability(self):
        if self.available_department:
            self.available_department = False
        else:
            self.available_department = True

    def set_department(self):
        if self.available_department:
            assignment = self.get_random_departments()
        else:
            assignment = "not assigned"
        return assignment

    def get_random_departments(self):
        return self._department[random.randint(0, len(self._department))]


class Bike:

    def __init__(self):
        self._bike = {"license": "", "color": "", "type": "", "status": "",
                      "owner": "", "date": "", "description": "", "address": ""}

    @staticmethod
    def recorded_incident():
        return "Se ha registrado un el incidente"

    def set_bike(self, test):               # REFACTORIZAR
        counter = 0
        for i in self._bike.keys():
            self._bike[i] = test[counter]
            counter += 1
        self._bike["department"] = Department().set_department()

    def get_department(self):
        return self._bike["department"]

    def get_bike(self):
        return self._bike

    def set_status(self):
        return self._bike["status"]

    def get_status(self):                   # FALTA API SENDGRID
        self._bike["status"] = "encontrada"
