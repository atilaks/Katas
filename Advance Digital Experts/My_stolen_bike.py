class Bike:

    def __init__(self):
        self._bike = {"license": "", "color": "", "type": "", "status": "",
                      "owner": "", "date": "", "description": "", "address": ""}

    def recorded_incident(self):
        return "Se ha registrado un el incidente"

    def set_bike(self, test):               # REFACTORIZAR
        counter = 0
        for i in self._bike.keys():
            self._bike[i] = test[counter]
            counter += 1

    def get_bike(self):
        return self._bike
