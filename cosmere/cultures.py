"""Roshar Cultures"""
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
