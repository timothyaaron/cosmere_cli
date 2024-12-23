"""Roshar Weapons"""
import random

from utils import MetaEnum


class Die:
    """A singular Dice"""
    def __init__(self, sides):
        self.sides = sides

    def roll(self):
        return random.randint(1, self.sides)


class Dice(metaclass=MetaEnum):
    FOUR = Die(4)
    SIX = Die(6)
    EIGHT = Die(8)
    TEN = Die(10)
    TWENTY = Die(20)


class Traits(metaclass=MetaEnum):
    CUMBERSOME = "Cumbersome"
    DANGEROUS = "Dangerous"
    DEADLY = "Deadly"
    DEFENSIVE = "Defensive"
    DISCREET = "Discreet"
    INDIRECT = "Indirect"
    LOADED = "Loaded"
    LOSES_DANGEROUS = "Loses Dangerous"
    LOSES_TWO_HANDED = "Loses Two-Handed"
    MOMENTUM = "Momentum"
    OFFHAND = "Offhand"
    PIERCE = "Pierce"
    PRESENTABLE = "Presentable"
    QUICKDRAW = "Quickdraw"
    THROWN = "Thrown"
    THROWN_S = "Thrown (Ranges.SMALL)"
    THROWN_M = "Thrown (Ranges.MEDIUM)"
    TWO_HANDED = "Two_handed"
    UNIQUE = "Unique"


class Ranges(metaclass=MetaEnum):
    MELEE = (0, 5)
    MELEE_5 = (0, 10)
    SMALL = (20, 60)
    MEDIUM = (30, 120)
    LARGE = (80, 320)
    HUGE = (100, 400)
    INSANE = (150, 600)


class DamageTypes(metaclass=MetaEnum):
    IMPACT = "Impact"
    KEEN = "Keen"
    SPIRIT = "Spirit"


class Categories(metaclass=MetaEnum):
    LIGHT = "Light"
    HEAVY = "Heavy"
    SPECIAL = "Special"
    ARMOR = "Armor"


class Weapon:
    def __init__(self, name, description, category, damage, damage_type, range_,
                 traits, expert_traits, weapons_skill, price):
        self.name: str = name
        self.description = description
        self.category = category
        self.damage = damage
        self.damage_type = damage_type
        self.range = range_
        self.traits: list[Traits] = traits
        self.expert_traits = expert_traits
        self.weapons_skills = weapons_skill
        self.price = price

    def __repr__(self):
        return self.name

    def roll_damage(self):
        return sum([d.roll() for d in self.damage])


class Weapons(metaclass=MetaEnum):
    JAVELIN = Weapon(
        name="Javelin", description="A short and sturdy spear made for throwing.",
        category=Categories.LIGHT, weapons_skill="Light",
        damage=[Dice.SIX], damage_type=DamageTypes.KEEN, range_=Ranges.MEDIUM,
        traits=[Traits.THROWN_M], expert_traits=[Traits.INDIRECT],
        price=20)
    KNIFE = Weapon(
        name="Knife", description="A small knife that is easy to conceal. Great for getting rid of people quickly and quietly.",
        category=Categories.LIGHT, weapons_skill="Light",
        damage=[Dice.FOUR], damage_type=DamageTypes.KEEN, range_=Ranges.MELEE,
        traits=[Traits.DISCREET], expert_traits=[Traits.THROWN_S, Traits.OFFHAND],
        price=8)
    MACE = Weapon(
        name="Mace", description="A small spiked club.",
        category=Categories.LIGHT, weapons_skill="Light",
        damage=[Dice.SIX], damage_type=DamageTypes.IMPACT, range_=Ranges.MELEE,
        traits=[], expert_traits=[Traits.MOMENTUM],
        price=20)
    RAPIER = Weapon(
        name="Rapier", description="A small light sword meant for quick and precise hits",
        category=Categories.LIGHT, weapons_skill="Light",
        damage=[Dice.SIX], damage_type=DamageTypes.KEEN, range_=Ranges.MELEE,
        traits=[Traits.QUICKDRAW], expert_traits=[Traits.DEFENSIVE],
        price=100)
    SHORTSPEAR = Weapon(
        name="Shortspear", description="A spear that is smaller than a normal spear. Making it much more effective for closer combat",
        category=Categories.LIGHT, weapons_skill="Light",
        damage=[Dice.EIGHT], damage_type=DamageTypes.KEEN, range_=Ranges.MELEE,
        traits=[Traits.TWO_HANDED], expert_traits=[Traits.THROWN_S],
        price=10)
    SIDESWORD = Weapon(
        name="Sidesword", description="The typical sword for your everydat militia men",
        category=Categories.LIGHT, weapons_skill="Light",
        damage=[Dice.SIX], damage_type=DamageTypes.KEEN, range_=Ranges.MELEE,
        traits=[Traits.QUICKDRAW], expert_traits=[Traits.OFFHAND],
        price=40)
    STAFF = Weapon(
        name="Staff", description="A sturdy stick meant for battle.",
        category=Categories.LIGHT, weapons_skill="Light",
        damage=[Dice.SIX], damage_type=DamageTypes.IMPACT, range_=Ranges.MELEE,
        traits=[Traits.TWO_HANDED, Traits.DISCREET], expert_traits=[Traits.DEFENSIVE],
        price=1)
    SHORTBOW = Weapon(
        name="Shortbow", description="A smaller bow meant for fast shooting, close range, and easier travel",
        category=Categories.LIGHT, weapons_skill="Light",
        damage=[Dice.SIX], damage_type=DamageTypes.KEEN, range_=Ranges.LARGE,
        traits=[Traits.TWO_HANDED], expert_traits=[Traits.QUICKDRAW],
        price=80)
    SLING = Weapon(
        name="Sling", description="Just like the one David used on Goliath.",
        category=Categories.LIGHT, weapons_skill="Light",
        damage=[Dice.SIX], damage_type=DamageTypes.IMPACT, range_=Ranges.MEDIUM,
        traits=[Traits.DISCREET], expert_traits=[Traits.INDIRECT],
        price=2)

    # Heavy Weapons
    AXE = Weapon(
        name="Axe", description="A simple battle axe.",
        category=Categories.HEAVY, weapons_skill="Heavy",
        damage=[Dice.SIX], damage_type=DamageTypes.KEEN, range_=Ranges.MELEE,
        traits=[Traits.THROWN_S], expert_traits=[Traits.OFFHAND],
        price=20)
    GREATSWORD = Weapon(
        name="Greatsword", description="A very large and sword meant not for the weak of heart.",
        category=Categories.HEAVY, weapons_skill="Heavy",
        damage=[Dice.TEN], damage_type=DamageTypes.KEEN, range_=Ranges.MELEE,
        traits=[Traits.TWO_HANDED], expert_traits=[Traits.DEADLY],
        price=200)
    HAMMER = Weapon(
        name="Hammer", description="Made specifically for smashing your enemies",
        category=Categories.HEAVY, weapons_skill="Heavy",
        damage=[Dice.TEN], damage_type=DamageTypes.IMPACT, range_=Ranges.MELEE,
        traits=[Traits.TWO_HANDED], expert_traits=[Traits.MOMENTUM],
        price=40)
    LONGSPEAR = Weapon(
        name="Longspear", description="A weapon to either help allies or keep enemyies at bay",
        category=Categories.HEAVY, weapons_skill="Heavy",
        damage=[Dice.EIGHT], damage_type=DamageTypes.KEEN, range_=Ranges.MELEE_5,
        traits=[Traits.TWO_HANDED], expert_traits=[Traits.DEFENSIVE],
        price=15)
    LONGSWORD = Weapon(
        name="Longsword", description="this sword is a bit larger than a normal sword.",
        category=Categories.HEAVY, weapons_skill="Heavy",
        damage=[Dice.EIGHT], damage_type=DamageTypes.KEEN, range_=Ranges.MELEE,
        traits=[Traits.TWO_HANDED], expert_traits=[Traits.LOSES_TWO_HANDED],
        price=60)
    POLEAXE = Weapon(
        name="Poleaxe", description="An axe that is put onto the end of a spear.",
        category=Categories.HEAVY, weapons_skill="Heavy",
        damage=[Dice.TEN], damage_type=DamageTypes.KEEN, range_=Ranges.MELEE,
        traits=[Traits.TWO_HANDED], expert_traits=[Traits.THROWN_S],
        price=40)
    SHIELD = Weapon(
        name="Shield", description="Not the best of weapons, yet it will protect you better than anything else.",
        category=Categories.HEAVY, weapons_skill="Heavy",
        damage=[Dice.FOUR], damage_type=DamageTypes.IMPACT, range_=Ranges.MELEE,
        traits=[Traits.DEFENSIVE], expert_traits=[Traits.OFFHAND],
        price=10)
    CROSSBOW = Weapon(
        name="Crossbow", description="The medival version of a gun.",
        category=Categories.HEAVY, weapons_skill="Heavy",
        damage=[Dice.EIGHT], damage_type=DamageTypes.KEEN, range_=Ranges.HUGE,
        traits=[Traits.TWO_HANDED, Traits.LOADED], expert_traits=[Traits.DEADLY],
        price=200)
    LONGBOW = Weapon(
        name="Longbow", description="A bow that is designed to shoot from far distances",
        category=Categories.HEAVY, weapons_skill="Heavy",
        damage=[Dice.SIX], damage_type=DamageTypes.KEEN, range_=Ranges.INSANE,
        traits=[Traits.TWO_HANDED], expert_traits=[Traits.INDIRECT],
        price=100)

    # Special Weapons
    UNARMED_ATTACK = Weapon(
        name="Unarmed Attack", description="An attack used without a weapon.",
        category=Categories.SPECIAL, weapons_skill="Athletics",
        damage=[Dice.FOUR], damage_type=DamageTypes.IMPACT, range_=Ranges.MELEE,
        traits=[Traits.UNIQUE], expert_traits=[Traits.MOMENTUM, Traits.OFFHAND],
        price=0,
    )  # damage=["Different per"], price="This is your hand. It didn't cost to get it."
    SHARDBLADE = Weapon(
        name="Shardblade", description="The leftover of a dead spren that was once bonded with a Kights Radiant. Now the most dangerous weapon on Roshar",
        category=Categories.SPECIAL, weapons_skill="Heavy",
        damage=[Dice.EIGHT, Dice.EIGHT], damage_type=DamageTypes.SPIRIT, range_=Ranges.MELEE,
        traits=[Traits.DANGEROUS, Traits.DEADLY, Traits.UNIQUE], expert_traits=[Traits.LOSES_DANGEROUS],
        price="Priceless")
    # RADIANT_SHARDBLADE


class Armor:
    def __init__(self, name, description, category, traits, expert_traits, deflect, price=0):
        self.name = name
        self.description = description
        self.category = category
        self.traits = traits
        self.expert_traits = expert_traits
        self.deflects = deflect
        self.price = price


class Armors(metaclass=MetaEnum):
    UNIFORM = Armor(
        name="Uniform", description="A uniform for your military group",
        category="Armor",
        traits=[Traits.PRESENTABLE],
        expert_traits=[],
        deflect=0
        )
    LEATHER = Armor(
        name="Leather", description="Won't protect from everything but it's good enough.",
        category="Armor",
        traits=[],
        expert_traits=[Traits.PRESENTABLE],
        deflect=1
    )
    CHAIN = Armor(
        name="Chain", description="The normal armor for any low level militia men.",
        category="Armor",
        traits=[Traits.CUMBERSOME],
        expert_traits=["Loses cumbersome"],
        deflect=2
    )
    BREASTPLATE = Armor(
        name="Breastplate", description="This armor makes you look like a soldier. Not really better than chain, just heavier.",
        category="Armor",
        traits=[Traits.CUMBERSOME],
        expert_traits=[Traits.PRESENTABLE],
        deflect=2
    )
    HALF_PLATE = Armor(
        name="Half Plate", description="Ok, now this is some good armor.",
        category="Armor",
        traits=[Traits.CUMBERSOME],
        expert_traits=[""],
        deflect=3
    )
    FULL_PLATE = Armor(
        name="Full Plate", description="You have finally obtained the best armor a soldier can get. Well besides Shardplate...",
        category="Armor",
        traits=[Traits.CUMBERSOME],
        expert_traits=["After all this work, nothing."],
        deflect=4
    )
