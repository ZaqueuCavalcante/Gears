from math import sqrt

def fatorTamanho(larguraDeFace, fatorFormaLewis, passoDiametral):
    return 1.192 * (larguraDeFace*sqrt(fatorFormaLewis)/passoDiametral)**0.0535
    