from enum import Enum


class Dice(Enum):
    FOUR = "1d4"
    SIX = "1d6"
    EIGHT = "1d8"
    TEN = "1d10"
    TWENTY = "1d20"


class Traits(Enum):
    CUMBERSOME = ()
    DANGEROUS = ()
    DEADLY = ()
    DEFENSIVE = ()
    DISCREET = ()
    INDIRECT = ()
    LOADED = ()
    MOMENTUM = ()
    OFFHAND = ()
    PIERCE = ()
    PRESENTABLE = ()
    QUICKDRAW = ()
    THROWN = ()
    TWO_HANDED = ()
    UNIQUE = ()


class Range(Enum):
    MELEE = (0, 5)
    MELEE_5 = (0, 10)
    SMALL = (20, 60)
    MEDIUM = (30, 120)
    LARGE = (80, 320)
    HUGE = (100, 400)
    INSANE = (150, 600)


class DamageTypes(Enum):
    KEEN = "Keen"
    IMPACT = "Impact"
    SPIRIT = "Spirit"


class Weapon:
    def __init__(self, name, description, type_, damage, damage_type, range_,
                 traits, expert_traits, weapons_skill, price):
        self.name: str = name
        self.description = description
        self.type = type_
        self.damage = damage
        self.damage_type = damage_type
        self.range = range_
        self.traits: list[Traits] = traits
        self.expert_traits = expert_traits
        self.weapons_skills = weapons_skill
        self.price = price
#Look at Javelin, Knife, Shorspear, and Axe. Thrown trait
#When there are two traits. Staff, Crossbow, Longsword, Unarmed attack, Shardblade
class Weapons(Enum):
    JAVELIN = Weapon(
        name="Javelin", 
        description="A short and sturdy spear made for throwing.", 
        type_="Light", 
        damage=Dice.SIX, 
        damage_type=DamageTypes.KEEN, 
        range_=Range.MEDIUM, 
        traits="Thrown(30/120)", 
        expert_traits=Traits.INDIRECT, 
        weapons_skill="Light", 
        price="20mk")
    KNIFE = Weapon(
        name="Knife", 
        description="A small knife that is easy to conceal. Great for getting rid of people quickly and quietly.", 
        type_="Light", 
        damage=Dice.FOUR, 
        damage_type=DamageTypes.KEEN, 
        range_=Range.MELEE, 
        traits=Traits.DISCREET, 
        expert_traits=Range.SMALL, 
        expert_traits=Traits.OFFHAND, 
        weapons_skill="Light", 
        price="8mk")
    MACE = Weapon(
        name="Mace", 
        description="A small spiked club.", 
        type_="Light", 
        damage=Dice.SIX, 
        damage_type=DamageTypes.IMPACT, 
        range_=Range.MELEE, 
        traits="none", 
        expert_traits=Traits.MOMENTUM, 
        weapons_skill="Light", 
        price="20mk")
    RAPIER = Weapon(
        name="Rapier", 
        description="A small light sword meant for quick and precise hits", 
        type_="Light", 
        damage=Dice.SIX, 
        damage_type=DamageTypes.KEEN, 
        range_=Range.MELEE, 
        traits=Traits.QUICKDRAW, 
        expert_traits=Traits.DEFENSIVE, 
        weapons_skill="Light", 
        price="100mk")
    SHORSPEAR = Weapon(
        name="Shortspear", 
        description="A spear that is smaller than a normal spear. Making it much more effective for closer combat", 
        type_="Light", 
        damage=Dice.EIGHT, 
        damage_type=DamageTypes.KEEN, 
        range_=Range.MELEE, 
        traits=Traits.TWO_HANDED, 
        expert_traits=Range.SMALL, 
        weapons_skill="Light", 
        price="10mk")
    SIDESWORD = Weapon(
        name="Sidesword", 
        description="The typical sword for your everydat militia men", 
        type_="Light", 
        damage=Dice.SIX, 
        damage_type=DamageTypes.KEEN, 
        range_=Range.MELEE, 
        traits=Traits.QUICKDRAW, 
        expert_traits=Traits.OFFHAND, 
        weapons_skill="Light", 
        price="40mk")
    STAFF = Weapon(
        name="Staff", 
        description="A sturdy stick meant for battle.", 
        type_="Light", 
        damage=Dice.SIX, 
        damage_type=DamageTypes.IMPACT, 
        range_=Range.MELEE, 
        traits=Traits.TWO_HANDED, traits=Traits.DISCREET, 
        expert_traits=Traits.DEFENSIVE, 
        weapons_skill="Light", 
        price="1mk")
    SHORTBOW = Weapon(
        name="Shortbow", 
        description="A smaller bow meant for fast shooting, close range, and easier travel", 
        type_="Light", 
        damage=Dice.SIX, 
        damage_type=DamageTypes.KEEN, 
        range_=Range.LARGE, 
        traits=Traits.TWO_HANDED, 
        expert_traits=Traits.QUICKDRAW, 
        weapons_skill="Light", 
        price="80mk")
    SLING = Weapon(
        name="Sling", 
        description="Just like the one David used on Goliath.", 
        type_="Light", 
        damage=Dice.SIX, 
        damage_type=DamageTypes.IMPACT, 
        range_=Range.MEDIUM, 
        traits=Traits.DISCREET, 
        expert_traits=Traits.INDIRECT, 
        weapons_skill="Light", 
        price="2mk")
#Heavy Weapons
    AXE = Weapon(
        name="Axe", 
        description="A simple battle axe.",
        damage=Dice.SIX, 
        damage_type=DamageTypes.KEEN,
        type_="Heavy", 
        range_=Range.MELEE, 
        traits="Thrown(20/60)",
        expert_tratis=Traits.OFFHAND, 
        weapons_skill="Heavy", 
        price="20mk")
    GREATSWORD = Weapon(
        name="Greatsword", 
        description="A very large and sword meant not for the weak of heart.", 
        type_="Heavy Weapons", 
        damage_type=DamageTypes.KEEN, 
        damage=Dice.TEN, 
        range_=Range.MELEE, 
        traits=Traits.TWO_HANDED, 
        expert_traits=Traits.DEADLY, 
        weapons_skill="Heavy", 
        price="200mk")
    HAMMER = Weapon(
        name="Hammer", 
        description="Made specifically for smashing your enemies", 
        type_="heavy", 
        damage=Dice.TEN, 
        damage_type=DamageTypes.IMPACT, 
        range_=Range.MELEE, 
        traits=Traits.TWO_HANDED, 
        expert_traits=Traits.MOMENTUM, 
        weapons_skill="Heavy", 
        price="40mk")
    LONGSPEAR = Weapon(
        name="Longspear", 
        description="A weapon to either help allies or keep enemyies at bay", 
        type_="Heavy", 
        damage=Dice.EIGHT, 
        damage_type=DamageTypes.KEEN, 
        range_=Range.MELEE_5, 
        traits=Traits.TWO_HANDED, 
        expert_traits=Traits.DEFENSIVE, 
        weapons_skill="Heavy", 
        price="15mk")
    LONGSWORD = Weapon(
        name="Longsword", 
        description="this sword is a bit larger than a normal sword.", 
        type_="Heavy", 
        damage=Dice.EIGHT, 
        damage_type=DamageTypes.KEEN, 
        range_=Range.MELEE, 
        traits=Traits.TWO_HANDED, 
        expert_traits="Loses two handed", 
        weapons_skill="Heavy", 
        price="60mk")
    POLEAXE = Weapon(
        name="Poleaxe", 
        description="An axe that is put onto the end of a spear.", 
        type_="Heavy", 
        damage=Dice.TEN, 
        damage_type=DamageTypes.KEEN, 
        range_=Range.MELEE, 
        traits=Traits.TWO_HANDED, 
        expert_traits=Range.MELEE_5, 
        weapons_skill="Heavy", 
        price="40mk")
    SHIELD = Weapon(
        name="Shield", 
        description="Not the best of weapons, yet it will protect you better than anything else.",
        type_="Heavy", 
        damage=Dice.FOUR, 
        damage_type=DamageTypes.IMPACT, 
        range_=Range.MELEE,
        traits=Traits.DEFENSIVE, 
        expert_traits=Traits.OFFHAND, 
        weapons_skill="Heavy", 
        price="10mk")
    CROSSBOW = Weapon(
        name="Crossbow", 
        description="The medival version of a gun.", 
        type_="Heavy", 
        damage=Dice.EIGHT, 
        damage_type=DamageTypes.KEEN, 
        range_=Range.HUGE,
        traits=Traits.TWO_HANDED, traits=Traits.LOADED, 
        expert_traits=Traits.DEADLY, 
        weapons_skill="Heavy", 
        price="200mk")
    LONGBOW = Weapon(
        name="Longbow", 
        description="A bow that is designed to shoot from far distances",
        type_="Heavy", 
        damage=Dice.SIX, 
        damage_type=DamageTypes.KEEN, 
        range_=Range.INSANE,
        traits=Traits.TWO_HANDED, 
        expert_traits=Traits.INDIRECT, 
        weapons_skill="Heavy", 
        price="100mk")
#Special Weapons
    UNARMED_ATTACK = Weapon(
        name="Unarmed Attack", 
        description="An attack used without a weapon.",
        type_="Special Weapons", 
        damage="Different per", 
        damage_type=DamageTypes.IMPACT, 
        range_=Range.MELEE,
        traits=Traits.UNIQUE, 
        expert_traits=Traits.MOMENTUM, 
        expert_traits=Traits.OFFHAND, 
        weapons_skill="Athletics", 
        price="This is your hand. It didn't cost to get it."
        )   
    SHARDBLADE = Weapon(
        name="Shardblade", 
        description="The leftover of a dead spren that was once bonded with a Kights Radiant. Now the most dangerous weapon on Roshar",
        type="Special Weapons", 
        damage=2*Dice.EIGHT, 
        damage_type=DamageTypes.SPIRIT, 
        range=Range.MELEE, 
        traits=Traits.DANGEROUS,
        traits=Traits.DEADLY,
        traits=Traits.UNIQUE, 
        expert_traits="Loses Dangerous", 
        weapons_skill="Heavy", 
        price="Priceless")

class Armor:
    def __init__(self, name, description, type_, traits, expert_traits, deflect, price):
        self.name = name
        self.description = description
        self.type = type_
        self.traits = traits
        self.expert_traits = expert_traits
        self.deflects = deflect
        self.price = price

class Armors(Enum):    
    UNIFORM = Armor(
        name="Uniform",
        description="A uniform for your military group",
        type="Armor",
        traits=Traits.PRESENTABLE,
        expert_traits="none",
        deflect=0
        )
    LEATHER = Weapon(
        name="Leather",
        description="Won't protect from everything but it's good enough.",
        type="Armor",
        traits="none",
        expert_traits=Traits.PRESENTABLE,
        deflect=1
    )
    CHAIN = Weapon(
        name="Chain",
        description="The normal armor for any low level militia men.",
        type="Armor",
        traits=Traits.CUMBERSOME,
        expert_traits="Loses cumbersome",
        deflect=2
    )
    BREASTPLATE = Weapon(
        name="Breastplate",
        description="This armor makes you look like a soldier. Not really better than chain, just heavier.",
        type="Armor",
        traits=Traits.CUMBERSOME,
        expert_traits=Traits.PRESENTABLE,
        deflect=2
    )
    HALF_PLATE = Weapon(
        name="Half Plate",
        description="Ok, now this is some good armor.",
        type="Armor",
        traits=Traits.CUMBERSOME,
        expert_traits="",
        deflect=3
    )
    FULL_PLATE = Weapon(
        name="Full Plate",
        description="You have finally obtained the best armor a soldier can get. Well besides Shardplate...",
        type="Armor",
        traits=Traits.CUMBERSOME,
        expert_traits="After all this work, nothing.",
        deflect=4
    )


    # RADIANT_SHARDBLADE