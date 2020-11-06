from math import sqrt

def fatorDinamico(numeroQualidade, velocidadeLinear):
    Q_v = numeroQualidade
    V = velocidadeLinear
    B = 0.25 * (12-Q_v)**(2/3)   # [] - Parâmetro auxiliar.
    A = 50 + 56*(1-B)   # [] - Parâmetro auxiliar.
    return ( (A + sqrt(V)) / A ) ** B   # [] - Fator dinâmico.
