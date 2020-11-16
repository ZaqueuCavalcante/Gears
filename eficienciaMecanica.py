from enum import Enum
from math import cos, tan, radians

class Condutor(Enum):
    pinhao = 0
    coroa = 1

def eficienciaMecanica(phi_n: float, lambda_avanco: float, f: float, condutor: Condutor):
    cos_phi = cos(radians(phi_n))
    tan_lambda = tan(radians(lambda_avanco))
    if (condutor.name == "pinhao"):
        return (cos_phi - f*tan_lambda) / (cos_phi + f/tan_lambda)
    if (condutor.name == "coroa"):
        return (cos_phi - f/tan_lambda) / (cos_phi + f*tan_lambda)
