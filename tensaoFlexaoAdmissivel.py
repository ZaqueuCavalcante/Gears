from enum import Enum

# Figuras 14-2 e 14-3.
class Dureza_TIPO(Enum):
    brinellGrau1 = 0
    brinellGrau2 = 1
    deNucleoGrau1 = 2
    deNucleoGrau2 = 3
    deNucleoGrau1Nitralloy = 4
    deNucleoGrau1Cromo = 5
    deNucleoGrau2Nitralloy = 6
    deNucleoGrau2Cromo = 7
    deNucleoGrau3Cromo = 8

def tensaoFlexaoAdmissivel(Dureza_TIPO, H_B):   # [psi]
    d = Dureza_TIPO.value
    if (d == 0):
        return 77.3*H_B + 12800
    elif (d == 1):
        return 102*H_B + 16400
    elif (d == 2):
        return 82.3*H_B + 12150
    elif (d == 3):
        return 108.6*H_B + 15890
    elif (d == 4):
        return 86.2*H_B + 12730
    elif (d == 5):
        return 105.2*H_B + 9280
    elif (d == 6):
        return 113.8*H_B + 16650
    elif (d == 7):
        return 105.2*H_B + 22280
    elif (d == 8):
        return 105.2*H_B + 29280
