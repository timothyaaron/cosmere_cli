"""Roshar Cultures"""
from typing import Self

from utils import MetaEnum


class Culture:
    """A Rosharian culture and the bonuses it provides."""
    def __init__(self, name, description="", bonuses=None):
        self.name: str = name
        self.description: str = description
        self.bonuses: str = bonuses


class Cultures(metaclass=MetaEnum):
    """Definitive list of cultures on Roshar."""
    ALETHI = Culture("Alethi")
    AZISH = Culture("Azish")
    HERDAZIAN = Culture("Herdazian")
    IRIALI = Culture("Iriali")
    KHARBRANTHIAN = Culture("Kharbranthian")
    LISTENER = Culture("Listener")
    NATAN = Culture("Natan")
    RESHI = Culture("Reshi")
    SHIN = Culture("Shin")
    TASHIKKI = Culture("Tashikki")
    THAYLEN = Culture("Thaylen")
    UNKALAKI = Culture("Unkalaki")
    VEDEN = Culture("Veden")


class Nation:
    name: str
    ethnicity: str
    capital: str
    neighbors: list[Self]
    language: None
    points_of_interest: list[str]


languages = {
    "Vorin": ("Alethi", "Veden", "Herdazian", "Thaylen", "Natan"),
    "Makabaki": ("Azish",),
    "Iri": ("Iriali", "Riran", "Reshi", "Selay", "Purelake"),
    "Dawnate": ("Shin", "Listener", "Unkalaki"),
    "Aimian": ("Siah", "Dysian"),
    "Spren": tuple(),  # each their own?
}
nations = [
    {"name": "Alethkar", "ethnicity": "Alethi", "capital": "Kholinar"},
    {"name": "Emul", "ethnicity": "Emuli", "capital": "Sesemalex Dar"},
    {"name": "Greater Hexi", "ethnicity": "Hexi", "capital": "Hexi City"},
    {"name": "Herdaz", "ethnicity": "Herdazian", "capital": None},
    {"name": "Iri", "ethnicity": "Iriali", "capital": None},
    {"name": "Jah Keved", "ethnicity": "Veden", "capital": "Vedenar"},
    {"name": "Kharbranth", "ethnicity": "Kharbranthian", "capital": "Kharbranth"},
    {"name": "Marat", "ethnicity": "Marati", "capital": None},
    {"name": "Reshi Isles", "ethnicity": "Reshi", "capital": None},
    {"name": "Shinovar", "ethnicity": "Shin", "capital": None},
    {"name": "Thaylenah", "ethnicity": "Thaylen", "capital": "Thaylen City"},
    {"name": "Triax", "ethnicity": "Triaxi", "capital": None},
    {"name": "Tu Bayla", "ethnicity": "Baylan", "capital": None},
    {"name": "Tu Fallia", "ethnicity": "Fallian", "capital": None},
    {"name": "Tukar", "ethnicity": "Tukari", "capital": None},
]
regions = [
    {"name": "Azish Empire", "within": "Makabak (almost all)", "capital": "Azimir"},
    {"name": "Horneater Peaks", "ethnicity": "Unkalaki (Horneaters)", "within": "Jah Keved"},
    {"name": "Makabak", "ethnicity": "Makabaki", "contains": [
        "Alm",
        "Azir",
        "Desh",
        "Emul",
        "Greater Hexi",
        "Liafor",
        "Marat",
        "Steen",
        "Tashikk",
        "Triax (about half)"
        "Tu Fallia",
        "Tukar",
        "Yezier",
    ]},

]
