from enum import Enum

# Figura 14-5.
class Dureza_TIPO(Enum):
    brinellGrau1 = 0
    brinellGrau2 = 1

def tensaoContatoAdmissivel(Dureza_TIPO, H_B):   # [psi]
    d = Dureza_TIPO.value
    if (d == 0):
        return 322*H_B + 29100
    elif (d == 1):
        return 349*H_B + 34300
