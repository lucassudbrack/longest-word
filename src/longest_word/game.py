# pylint: disable=missing-docstring
# pylint: disable=too-few-public-methods

import random
import string


class Game:
    def __init__(self) -> list:
        """Attribute a random grid of size 9"""
        self.grid = list(random.choices(string.ascii_uppercase, k = 9))

    def is_valid(self, word: str) -> bool:
        """Return True if and only if the word is valid, given the Game's grid"""
        if not word:
            return False

        word = word.upper()

        for w in list(word):
            if word.count(w) > self.grid.count(w):
                return False

        return True
