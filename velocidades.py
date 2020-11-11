from math import pi, cos, radians

def velocidadeDeslizamentoPinhao(d: float, n_W: int, lambda_avanco: float):
    return (pi*d*n_W)/(12*cos( radians(lambda_avanco) ))

def velocidadeLinear(diametro: float, n_W: int):
    return (pi*diametro*n_W)/(12)

def velocidadeAngular(n_W: int, m_G: int):
    return n_W/m_G
