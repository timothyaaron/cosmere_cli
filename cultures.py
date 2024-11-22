from enum import Enum


class Culture:
    def __init__(self, name, description="", bonuses=None):
        self.name: str = name
        self.description: str = description
        self.bonuses: str = bonuses


class Cultures(Enum):
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
