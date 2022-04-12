#!/usr/bin/env python
# -*- coding: utf-8 -*-

# EXTRA CREDIT:

# Create a program that will play the Greed Game.
# Rules for the game are in GREED_RULES.TXT.

# You already have a DiceSet class and score function you can use.
# Write a player class and a Game class to complete the project.  This
# is a free form assignment, so approach it however you desire.

from runner.koan import *
import re

class Game():
    def __init__(self):
        pass

    def get_score(self, input):
        set1 = 0
        len(re.search(1, input))
        return set1

class Player():
    pass


class AboutExtraCredit(Koan):
    # Write tests here. If you need extra test classes add them to the
    # test suite in runner/path_to_enlightenment.py
    def test_extra_credit_task(self):
        pass

    def test_three_ones_roll(self):
        #Arrange
        player1 = Player()
        expected = 1000

        #Act
        result = player1.get_score([1, 1, 1, 2, 2])

        #Assert
        self.assertEqual(expected, result)