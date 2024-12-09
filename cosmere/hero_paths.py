from utils import MetaEnum


class Specialty(metaclass=MetaEnum):
    ARCHER = "Archer"
    ASSASSIN = "Assassin"
    TRACKER = "Tracker"


class Talent(metaclass=MetaEnum):
    BACKSTEP = "Backstep"
    COMBAT_TRAINING = "Combat Training"
    EXPLOIT_WEAKNESS = "Exploit Weakness"
    HARDY = "Hardy"
    SEEK_QUARRY = "Seek Quarry"
    SHARP_EYE = "Sharp Eye"
    STEADY_AIM = "Steady Aim"
    TAGGING_SHOT = "Tagging Shot"
    UNRELENTING_SALVO = "Unrelenting Salvo"


class HeroPathNode:
    def __init__(self, name: Talent | Specialty, children: list=None):
        self.name = name
        self.children = children or []  # [HeroPathNode]


class HunterNodes(metaclass=MetaEnum):
    EXPLOIT_WEAKNESS = HeroPathNode(Talent.EXPLOIT_WEAKNESS)
    SHARP_EYE = HeroPathNode(Talent.SHARP_EYE, [EXPLOIT_WEAKNESS])
    TAGGING_SHOT = HeroPathNode(Talent.TAGGING_SHOT, [SHARP_EYE])

    BACKSTEP = HeroPathNode(Talent.BACKSTEP)
    UNRELENTING_SALVO = HeroPathNode(Talent.UNRELENTING_SALVO)
    HARDY = HeroPathNode(Talent.HARDY, [UNRELENTING_SALVO])
    STEADY_AIM = HeroPathNode(Talent.STEADY_AIM, [BACKSTEP, HARDY])
    COMBAT_TRAINING = HeroPathNode(Talent.COMBAT_TRAINING, [STEADY_AIM])


class Specialties(metaclass=MetaEnum):
    ARCHER = HeroPathNode(Specialty.ARCHER, [HunterNodes.TAGGING_SHOT, HunterNodes.COMBAT_TRAINING])
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


class HeroPaths(metaclass=MetaEnum):
    HUNTER = BaseHeroPath(
        "Hunter", starting_talent=Talent.SEEK_QUARRY,
        specialties=[Specialties.ARCHER, Specialties.ASSASSIN, Specialties.TRACKER],

    )


class HeroPath:
    def __init__(self, base: HeroPaths):
        self.base = base
        self.specialty = None
        self.talents = []
