import unittest
from KataDoom import *
   
class KataDoom_Test(unittest.TestCase):
    def test_name(self):
        #Arrange 
        name="Jaime!"
        player = Player()
        expected = "Jaime!" 
        player.set_name(name)

        #Act
        result=player.get_name()


        #Assert
        self.assertEqual(expected, result)

    def test_initial(self):
        #Arrange 
        name="Jaime!"
        player = Player()
        expected = "Welcome Jaime! Your PV is: 100 Your armour is: 50 Your damage is: 15" 
        player.set_name(name)

        #Act
        result=player.get_player_string()

        #Assert
        self.assertEqual(expected, result)

    def test_weapon1(self):
        #Arrange 
        weapon = Weapon()
        expected = ['Motosierra', 'No', 'Infinite', 'No', 30]

        #Act
        result=weapon.get_weapon(1)

        #Assert
        self.assertEqual(expected, result)

    # def test_random(self):
    #     #Arrange 
    #     weapon = Weapon()
    #     expected = ""

    #     #Act
    #     result = weapon.get_random_weapon()

    #     #Assert
    #     self.assertEqual(expected, result)

    # def test_player_weapon(self):
    #     #Arrange 
    #     player = Player()
    #     weapon1 = Weapon()
    #     weapon2 = Weapon()
    #     weapon3 = Weapon()
    #     player.weapons[0] = weapon1.get_random_weapon()
    #     player.weapons[1] = weapon2.get_random_weapon()
    #     player.weapons[2] = weapon3.get_random_weapon()
    #     expected = ""

    #     #Act
    #     result = player.get_weapons()

    #     #Assert
    #     self.assertEqual(expected, result)

    # def test_daemon_random(self):
    #     #Arrange
    #     daemon = Daemon()
    #     expected = ""
    #
    #     #Act
    #     result = daemon.get_random_daemon()
    #
    #     #Assert
    #     self.assertEqual(expected, result)

    # def test_daemon_random(self):
    #     #Arrange
    #     level = Level()
    #     expected = ""
    #
    #     #Act
    #     level.set_daemons()
    #     result = level.get_daemons()
    #
    #     #Assert
    #     self.assertEqual(result, expected)

    def test_1_random_weapon(self):
        #Arrange
        player = Player()
        level = Level()
        weapon = Weapon()
        expected = weapon.get_dictionary()

        #Act
        player.set_weapon(weapon.get_random_weapon())
        result = player.get_weapons()

        #Assert
        # self.assertTrue(result, expected.values())

        headers = ["name", "ammo_tipe", "capacity", "ammo_per_shot", "damage"]
        # headers = expected.values()[0].keys()
        element_there = False
        for element in weapon.get_weapon_array:
            if element_there == False:
                element_there = result[0] in element.values()

        print("0000000000000")
        # print(expected.values())
        ramon = {headers[i]: result[0][i] for i in range(0,len(result[0]))}
        a = {1:2, 2:5, 3:6, 4:7}
        b = {1:2}
        # print()
        # print(result[0])
        # print("0000000000000")
        # print(weapon.get_weapon_values())
        # print(ramon)
        # print("cosa" if ramon in expected.values() else "")
        # print("0000000000000")
        # print(expected)

        self.assertTrue(ramon in expected)
        print()

    # def test_3_random_weapons(self):
    #     #Arrange
    #     level = Level()
    #     expected = ""
    #     player = Player()
    #
    #     #Act
    #     result = player.get_weapons()
    #
    #     #Assert
    #     self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main() 