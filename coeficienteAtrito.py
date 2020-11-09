from math import exp

def coeficienteAtrito(V_S: float):
    if (V_S == 0):
        return 0.15
    if (V_S > 0 and V_S <= 10):
        return 0.124*exp(-0.074*V_S**(0.645))
    return 0.103*exp(-0.110*V_S**(0.450)) + 0.012
