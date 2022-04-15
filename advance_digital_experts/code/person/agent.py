from code.person.individual import Individual
# TODO: METER INDIVIDUAL EN EL INIT


class Agent(Individual):
    def __init__(self, agent):
        super().__init__(agent)
        self._police_id = agent["police id"]
        self._department = agent["department"]
        self._manager = agent["manager"]  # TODO: CAMBIAR A RANGOS

    @property
    def full_description(self):             # TODO: HACER CONCATENACIÓN DE DICCIONARIOS
        return {"name": self._name, "surname": self._surname, "passport": self._passport,
                "police id": self.police_id, "department": self.department, "manager": self.manager}
    # TODO: CAMBIAR LOS GETERS PARA QUE ACCEDA DESDE EL SET

    @property
    def police_id(self):
        return self._police_id

    @police_id.setter
    def police_id(self, new_police_id):
        self._police_id = new_police_id

    @property
    def department(self):
        return self._department

    @property
    def manager(self):
        return self._manager
