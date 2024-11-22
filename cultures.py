from enum import Enum

class culture:
    def __innit__(self, name, description, bonuses):
        self.name = name
        self.description = description
        self.bonuses = bonuses

class cultures(Enum):
    ALETHI
    AZISH
    HERDAZIAN
    KHARBRANTHIAN
    RESHI
    SHIN
    TASHIKKI
    THAYLEN
    UNKALAKI
    VEDEN

    IRIALI
    LISTENER
    NATAN