from math import exp

def fatorVelocidade(V_S: float):
    if (V_S < 700):
        return 0.659*exp(-0.0011*V_S)
    if (V_S >= 700 and V_S <= 3000):
        return 13.31*V_S**(-0.571)
    return 65.52*V_S**(-0.774)
