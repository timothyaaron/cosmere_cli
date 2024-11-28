"""A Cosmere RPG Text User Interface"""
from prompt_toolkit import prompt
from prompt_toolkit.completion import FuzzyWordCompleter

from cosmere.character import Character
from cosmere.cultures import Cultures


name = prompt("What's your character's name? ")
character = Character(name)

selections = FuzzyWordCompleter([c.name for c in Cultures])
culture = prompt('Choose a culture: ', completer=selections)
character.culture = Cultures[culture]

print(character)
