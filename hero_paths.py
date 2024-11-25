from enum import Enum


class Specialty(Enum):
    ARCHER = "Archer"
    ASSASSIN = "Assassin"
    TRACKER = "Tracker"


class Talent(Enum):
    HARDY = "Hardy"
    SEEK_QUARRY = "Seek Quarry"
    UNRELENTING_SALVO = "Unrelenting Salvo"


class HeroPathNode:
    def __init__(self, name: Talent | Specialty, children: list=None):
        self.name = name
        self.children = children or []  # [HeroPathNode]


class HunterTalents(Enum):
    UNRELEATING_SALVO = HeroPathNode(Talent.UNRELENTING_SALVO)
    HARDY = HeroPathNode(Talent.HARDY, [UNRELEATING_SALVO])


class Specialties(Enum):
    ARCHER = HeroPathNode(Specialty.ARCHER, [])
    ASSASSIN = HeroPathNode(Specialty.ASSASSIN, [])
    TRACKER = HeroPathNode(Specialty.TRACKER, [])


class BaseHeroPath:
    def __init__(self,
                 name: str,
                 starting_talent: Talent,
                 specialties: list[HeroPathNode],
                 talent_tree:
    ):
        self.name = name
        self.starting_talent: Talent = talent
        self.specialties = specialties


class HeroPaths(Enum):
    HUNTER = BaseHeroPath(
        "Hunter", starting_talent=Talent.SEEK_QUARRY,
        specialties=[Specialties.ARCHER, Specialties.ASSASSIN, Specialties.TRACKER],

    )


class HeroPath:
    def __init__(self, base: HeroPaths):
        self.base = base
