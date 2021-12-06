import unittest
from unittest import result

class Game:
    def __init__(self):
        self.PUNTUACION_MINIMA = 300
        self.PUNTUACION_DETONANTE_DE_FINAL = 3000
        self._roll_score = True                 #Detonante de puntuación constante
        self._lower = True                      #Detonante de mínimo puntuable
        self.check_end = False                  #Detonante de fin de partida
        self.last_game = False
        self.player_score_mierder = 0
        self.players = [Player(), Player()]

    def read_dices_ok(self, roll):                 #Lee la tirada
        for i in self.players:
            pass



    

    def get_winner(self, player1, player2):
        self.player1._score = self.get_score(self.player1.roll)
        self.player2._score = self.get_score(self.player2.roll)

    def get_score(self, input):                 #Función principal
        self.read_dice_ok(input)
        self.get_value_to_roll()
        self.min_score()
        result = self.can_scoring()
        if self.check_end == True: 
            result = self.last_score() 
        return result

    def can_scoring(self):                      #Finde ronda o indice de puntuación
        result = "Has terminado tu ronda. Tu puntuació es de: 0"
        if self._roll_score == True and self._lower == True:
            result = "Tu puntuació es de: " + str(self.player1._score)
            if self.player_score_mierder >= self.PUNTUACION_DETONANTE_DE_FINAL: 
                self.check_end = True
        return result

    def last_score(self):                       #Fin de partida
        if self.last_game == False:
            result = "Has detonado el final de partida. Tu puntuación final es: " + str(self.player1._score) + ". El resto de jugadores tiene una última oportunidad de puntuar."
            self.last_game = True
        else:
            result = "Has terminado tu partida con una puntuación final de: " + str(self.player1._score)
        return result

    def set_roll(self, roll1, roll2):
        self.player1.roll = roll1
        self.player1.roll = roll2

    def min_score(self):                        #Mínimo puntuable
        if self.player_score_mierder < self.PUNTUACION_MINIMA: 
            self._lower = False

    def ramon(self, roll):

        return self.get_score(roll)

class Player:
    def __init__(self):
        self._score = 0                         #Puntuación
        self._repeats = []      #Repeticiones de valores
        self._roll = [0, 0, 0, 0, 0, 0]

    def get_value_to_roll(self):                #Puntua la tirada
        old_score = self._score
        for i in range(1, 7):
            if self._repeats[i - 1] >= 3:
                if i == 1: self._score += 1000
                else: self._score += i * 100
                self._repeats[i - 1] -= 3
        self.__unique_scores()
        if old_score == self._score: self._roll_score = False
        
    def __unique_scores(self):                    #Puntuaciones extra
        self._score += self._repeats[0] * 100
        self._score += self._repeats[4] * 50

    def set_repeat_dice(self):
        result = []
        for i in range(1, 7):
            result[i - 1] = self._roll.count(i)
            self.set_repeats(result)

    def set_roll(self, input):
        self._roll = input

    def get_roll(self):
        return self._roll

    def set_repeats(self, input):
        self._repeats = input

    