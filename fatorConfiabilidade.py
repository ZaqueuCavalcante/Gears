from scipy.interpolate import interp1d

confiabilidades = [0.9999, 0.999, 0.99, 0.90, 0.50]
fatores = [1.50, 1.25, 1.00, 0.85, 0.70]

def fatorConfiabilidade(confiabilidade):
    fator = interp1d(confiabilidades, fatores)
    return fator(confiabilidade)
