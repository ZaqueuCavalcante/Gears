from math import log

confiabilidades = [0.9999, 0.999, 0.99, 0.90, 0.50]
fatores = [1.50, 1.25, 1.00, 0.85, 0.70]

def fatorConfiabilidade(confiabilidade):
    R = confiabilidade
    if (R in confiabilidades):
        index = confiabilidades.index(R)
        return fatores[index]
    elif (R > 0.5 and R < 0.99):
        return 0.658 - 0.0759*log(1-R)
    elif (R >= 0.99 and R <= 0.9999):
        return 0.500 - 0.109*log(1-R)
