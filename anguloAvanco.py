phi_n_values = [14.5, 20, 25, 30]
lambda_max_values = [16, 25, 35, 45]
from math import atan, degrees, pi

def anguloAvanco(L: float, d: float, phi_n: float):
    if (phi_n in phi_n_values):
        lambda_avanco = degrees( atan(L/(pi*d)) )

        lambda_max = getLambdaMax(phi_n)
        if (lambda_avanco > lambda_max):
            return "lambda_avanco = {} e lambda_max = {}".format(lambda_avanco, lambda_max)
        return lambda_avanco

    else:
        return "phi_n inválido."

def getLambdaMax(phi_n: float):
    index = phi_n_values.index(phi_n)
    return lambda_max_values[index]
