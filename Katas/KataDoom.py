from unittest import result
import random

class Game:
    def __init__(self):
        self._level = Level()
        self._is_clear_daemons = False

    def get_random(self,list):
        return random.randint(0,len(list))

class Player():
    def __init__(self): 
        self._armour = 50
        self._PV = 100
        self._damage = 15
        self._name = ""
        self._weapons = [Weapon(), Weapon(), Weapon(), Weapon(), Weapon()]
        
    def get_armour(self):
        return self._armour

    def set_armour(self, armour):
        self._armour = armour

    def get_PV(self):
        return self._PV

    def set_PV(self, pv):
        self._PV = pv

    def get_name(self):
        return self._name
    
    def get_damage(self):
        return self._damage

    def set_name(self, name):
        self._name = name

    def get_player_string(self):
        result = "Welcome " + str(self.get_name()) + " Your PV is: " + str(self.get_PV()) + " Your armour is: " + str(self.get_armour()) + " Your damage is: " + str(self.get_damage())
        return result

    def get_weapons(self):
        return self._weapons

    def set_weapon(self, weapon):
        for i in range(5):
            if self._weapons[i] not in Weapon()._weapon_dictionary.values():
                self._weapons[i] = weapon
                break

    def set_random_weapon(self):
        self.set_weapon(Weapon().get_random_weapon())

    def set_random_weapons(self, counter):
        for i in range(counter):
            self.set_random_weapon()

class Weapon(Game):
    def __init__(self):
        self._weapon_dictionary = [
            {"name":"Motosierra","ammo_tipe":"No","capacity":"Infinite","ammo_per_shot":"No","damage":30},
            {"name":"Pistola","ammo_tipe":"Bala","capacity":200,"ammo_per_shot":1,"damage":15},
            {"name":"Escopeta","ammo_tipe":"Cartucho","capacity":30,"ammo_per_shot":1,"damage":50},
            {"name":"Ametralladora","ammo_tipe":"Bala","capacity":200,"ammo_per_shot":10,"damage":150},
            {"name":"Lanzamisiles","ammo_tipe":"Misil","capacity":20,"ammo_per_shot":1,"damage":200},
            {"name":"PistolaPlasma","ammo_tipe":"Plasma","capacity":200,"ammo_per_shot":10,"damage":200},
            {"name":"BFG9000","ammo_tipe":"Plasma","capacity":200,"ammo_per_shot":50,"damage":1000}
            ]

    # def get_weapon_values(self):
    #     return self._weapon_dictionary.values()

    def get_dictionary(self):
        return self._weapon_dictionary

    def get_weapon(self,position):
        result = []
        result.append(self._weapon_dictionary[position]['name'])
        result.append(self._weapon_dictionary[position]['ammo_tipe'])
        result.append(self._weapon_dictionary[position]['capacity'])
        result.append(self._weapon_dictionary[position]['ammo_per_shot'])
        result.append(self._weapon_dictionary[position]['damage'])
        return result

    def get_random_weapon(self):
        return self.get_weapon(self.get_random(self._weapon_dictionary))

class Daemon(Game):
    def __init__(self):
        # self._name = ""
        # self._PV = 0
        # self._damage = 0
        self._daemon_dictionary = {
            1:{"name":"Zombi","PV":"50","damage":"4"},
            2:{"name":"Escopetero","PV":"60","damage":"6"},
            3:{"name":"Diablillo","PV":"70","damage":"8"},
            4:{"name":"Demonio","PV":"80","damage":"10"},
            5:{"name":"Espectro","PV":"80","damage":"10"},
            6:{"name":"Alma perdida","PV":"45","damage":"6"},
            7:{"name":"Cacodemon","PV":"215","damage":"10"},
            8:{"name":"Barón","PV":"230","damage":"12"},
            9:{"name":"Cyberdemon","PV":"500","damage":"16"},
            10:{"name":"Araña Cerebro","PV":"600","damage":"18"}
            }

    def get_daemon(self, position):
        result = []
        result.append(self._daemon_dictionary[position]['name'])
        result.append(self._daemon_dictionary[position]['PV'])
        result.append(self._daemon_dictionary[position]['damage'])
        return result

    def get_random_daemon(self):
        return self.get_daemon(self.get_random(self._daemon_dictionary))

class Level:
    def __init__(self):
        self._daemons = [Daemon(), Daemon(), Daemon(), Daemon(), Daemon(), Daemon()]
        Player().set_PV(100)
        Player().set_armour(50)
        # Player().set_random_weapons(3)

    def set_daemons(self):
        for i in range(6):
            self._daemons[i] = Daemon().get_random_daemon()

    def get_daemons(self):
        return self._daemons
