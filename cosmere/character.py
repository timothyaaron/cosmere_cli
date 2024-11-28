"""Roshar Characters"""

class Character:
    def __init__(self, name):
        self.name = name
        self.culture = None

    def __repr__(self):
        return f"{self.name} is {self.culture}"
