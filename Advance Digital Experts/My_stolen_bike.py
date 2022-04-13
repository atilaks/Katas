class Bike:

    def __init__(self):
        self._bike = {"license": "", "color": "", "type": "", "status": "",
                      "owner": "", "date": "", "description": "", "address": ""}

    def recorded_incident(self):
        return "Se ha registrado un el incidente"

    def set_bike(self, test):
        for i in range(0,7):
            self._bike[i][test[i]]
            i++

