class Game:
    def __init__(self):
        self.oxygen = 150               # Oxigeno del buceador
        self.depth = 0                  # Profundidad del buceador
        self.move = 1                   # Movimiento por defecto
        self.points = 0                 # Puntuación

    def core_method(self, action):      # Función principal
        if self.depth == 0 and action == "Up":
            return "No puedes subir más"
        self.set_action(action)
        if self.oxygen == 0 or self.depth == 0:
            return self.check_end_game()
        else:
            return self.get_status()

    def get_oxygen(self):               # Devuelve el nivel actual de oxígeno
        return "Oxígeno: " + str(self.oxygen)

    def get_depth(self):                # Devuelve el nivel actual de profundidad
        return "Profundidad: " + str(self.depth)

    def get_points(self):               # Devuelve la cantidad actual de puntos
        return "Puntos: " + str(self.points)

    def get_status(self):               # Devuelve el estado actual de profundiad y oxígeno
        return self.get_oxygen() + "\n" + \
               self.get_depth() + "\n" + \
               self.get_points()

    def check_end_game(self):           # Detonantes de fin de partida
        if self.oxygen <= 0:
            return "Mueres. No puntúas"
        else:
            return "Has terminado la partida.\n" + self.get_points()

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

    def set_points(self):               # Suma puntos
        self.points += self.depth

    def set_parameters(self, oxygen, depth):
        self.oxygen = oxygen
        self.depth = depth
