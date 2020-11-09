from enum import Enum
from math import log10

class Fundicao(Enum):
    areia = 0
    resfriamento = 1
    centrifuga = 2

def fatorMateriais(C: float, D_m: float, tipoFundicao: Fundicao):
    if (C <= 3):
        return 720 + 10.37*C**3
    if (tipoFundicao.name == "areia"):
        if (D_m <= 2.5):
            return 1000
        return 1190 - 477*log10(D_m)
    if (tipoFundicao.name == "resfriamento"):
        if (D_m <= 8):
            return 1000
        return 1412 - 456*log10(D_m)
    if (tipoFundicao.name == "centrifuga"):
        if (D_m <= 25):
            return 1000
        return 1251 - 180*log10(D_m)
