import unittest
from unittest import result

class Game:
    def __init__(self):
        self.PUNTUACION_MINIMA = 300
        self.PUNTUACION_DETONANTE_DE_FINAL = 3000
        self.las_round = False                  #Detonante de fin de partida
        self.last_game = False
        self.players = [Player(), Player()]

    def funcon_de_entrada(self, roll):

        self.get_score(roll)

    def get_ok_score(self):                     #COMPRUEBA LAS NORMAS DE PUNTUACION
        self.min_score()
        for i in self.players:
            if self.players[i]._greater_0 == True:
                print("Fin de ronda")
            elif self.players[i]._lower == True:
                print("Puedes volver a tirar")

    def set_rolls(self, input):                 #RECIBE LA TIRADA EN PARALELO
        for i in self.players:
            self.players[i].set_roll(input)

    def min_score(self):                        #MINIMO PUNTUABLE
        for i in self.players:
            if self.players[i]._score >= self.PUNTUACION_MINIMA: 
                self.players[i]._lower = True

    def get_score(self, input):                 #DA EL SCORE (sin normas)
        self.set_rolls(input)
        for i in self.players:
            self.players[i].get_value_to_roll()

    def detonating_end_game(self):              #DETONANTE DE FIN DE PARTIDA
        for i in self.players:
            if self.players[i]._score >= self.PUNTUACION_DETONANTE_DE_FINAL and self.last_round == False:
                self.last_game = True
                self.las_round = True
                print("Última ronda. Tu puntuación es: " + str(self.players[i]._score)

    def last_roud(self):                        #FALTA 
        for i in self.players:
            pass

    def get_winner(self):
        if 

    def get_winner(self, player1, player2):
        self.player1._score = self.get_score(self.player1.roll)
        self.player2._score = self.get_score(self.player2.roll)

    def last_score(self):                       #Fin de partida
        if self.last_game == False:
            result = "Has detonado el final de partida. Tu puntuación final es: " + str(self.player1._score) + ". El resto de jugadores tiene una última oportunidad de puntuar."
            self.last_game = True
        else:
            result = "Has terminado tu partida con una puntuación final de: " + str(self.player1._score)
        return result

    # def read_dices_ok(self, roll):                 
    #     self.set_roll(roll)

    # result = self.can_scoring()
    # if self.check_end == True: 
    #     result = self.last_score() 
    # return result

    # def can_scoring(self):                      #Finde ronda o indice de puntuación
    #     result = "Has terminado tu ronda. Tu puntuació es de: 0"
    #     if self._roll_score == True and self._lower == XXXX:
    #         result = "Tu puntuació es de: " + str(self.player1._score)
    #         if self.player_score_mierder >= self.PUNTUACION_DETONANTE_DE_FINAL: 
    #             self.check_end = True
    #     return result



class Player:
    def __init__(self):
        self._score = 0                         #Puntuación
        self._repeats = []      #Repeticiones de valores
        self._roll = [0, 0, 0, 0, 0, 0]
        self._lower = False                      #Detonante de mínimo puntuable
        self._greater_0 = False                 #Detonante de puntuación constante

    def get_value_to_roll(self):                #Puntua la tirada
        old_score = self._score
        for i in range(1, 7):
            if self._repeats[i - 1] >= 3:
                if i == 1: self._score += 1000
                else: self._score += i * 100
                self._repeats[i - 1] -= 3
        self.__unique_scores()
        if old_score == self._score: self._greater_0 = True
        
    def __unique_scores(self):                    #Puntuaciones extra
        self._score += self._repeats[0] * 100
        self._score += self._repeats[4] * 50

    def set_repeat_dice(self):
        result = []
        for i in range(1, 7):
            result[i - 1] = self._roll.count(i)
            self.set_repeats(result)

    def set_roll(self, input):                      #MODIFICA _ROLL
        self._roll = input

    def get_roll(self):                             #DEVUELVE _ROLL
        return self._roll

    def set_repeats(self, input):
        self._repeats = input