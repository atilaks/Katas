class Bike:

    def __init__(self):
        self._bike = {"license": "", "color": "", "type": "", "status": "",
                      "owner": "", "date": "", "description": "", "address": ""}

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

    def get_address(self):
        return self._bike["address"]

    def set_address(self):                  # FALTA API GOOGLE
        self._bike["address"] = ""

# MANDAR A USUARIO
#     @staticmethod
#     def recorded_incident():
#         return "Se ha registrado un el incidente"
