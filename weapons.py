from enum import Enum


class Dice(Enum):
    FOUR = '1d4'
    SIX = '1d6'


class DamageTypes(Enum):
    KEEN = 'Keen'
    IMPACT = 'Impact'
    SPIRIT = 'Spirit'


class Weapon:
    def __init__(self, name, description, type_, damage, damage_type, range_,
                 traits, expert_traits, weapons_skill, price):
        self.name = name
        self.description = description
        self.type = type_
        self.damage = damage
        self.damage_type = damage_type
        self.range = range_
        self.traits = traits
        self.expert_traits = expert_traits
        self.weapons_skills = weapons_skill
        self.price = price


class Weapons(Enum):
    AXE = Weapon("Axe", "A simple battle axe.", damage='1d6', damage_type=DamageTypes.KEEN)
