class Bike:

    def __init__(self):
        self._bike = {"license": "", "color": "", "type": "", "status": "",
                      "owner": "", "date": "", "description": "", "address": ""}

    def set_bike(self, test):               # REFACTORIZAR
        counter = 0
        for i in self._bike.keys():
            self._bike[i] = test[counter]
            counter += 1

    def get_bike(self):
        return self._bike

    def set_status(self):
        return self._bike["status"]

    def get_status(self):                   # FALTA API SENDGRID
        self._bike["status"] = "encontrada"

    def set_address(self):                  # FALTA API GOOGLE
        self._bike["address"] = ""

    def get_address(self):
        return self._bike["address"]

