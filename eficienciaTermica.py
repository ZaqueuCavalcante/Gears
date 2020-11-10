from enum import Enum
from math import cos, tan, radians

class Eixo(Enum):
    semVentilador = 0
    comVentilador = 1

def eficienciaTermicaGeral(n_w: float, eixo: Eixo):
    if (eixo.name == "semVentilador"):
        return n_w/6494 + 0.13
    if (condutor.name == "comVentilador"):
        return n_w/3939 + 0.13
