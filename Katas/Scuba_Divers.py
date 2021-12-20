class Game:
    def __init__(self):
        self.oxygen = 150               # Oxigeno del buceador
        self.depth = 0                  # Profundidad del buceador
        self.sea_level_flag = False     # Flag nivel del mar
        self.move = 1                   # Movimiento por defecto
        self.points = 0                 # Puntuación

    def get_oxygen(self):               # Devuelve el nivel actual de oxígeno
        return self.oxygen

    def get_depth(self):                # Devuelve el nivel actual de profundidad
        return self.depth

    def get_status(self):               # Devuelve el estado actual de profundiad y oxígeno
        if self.oxygen <= 0:
            return "Mueres. No puntúas"
        return "Oxígeno: " + str(self.oxygen) + ". Profundidad: " + str(self.depth)

    def get_points(self):
        return self.points

    def set_action(self, action):       # Determina la acción
        if action == "Down":
            self.set_action_down()
        elif action == "Up":
            self.set_action_up()
        elif action == "Keep":
            self.set_action_keep()
        self.set_points()

    def set_action_down(self):          # Acción de bajar
        self.depth += self.move
        self.oxygen -= self.depth * 2

    def set_action_up(self):            # Acción de subir
        self.depth -= self.move
        self.oxygen -= self.move

    def set_action_keep(self):          # Acción de mantenerse
        self.oxygen -= self.move / 2

    def set_points(self):
        self.points += self.depth

    def set_parameters(self, oxygen, depth):
        self.oxygen = oxygen
        self.depth = depth
