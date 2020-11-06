from enum import Enum

class C_mc_TIPO(Enum):
    dentesNaoCoroados = 1.00
    dentesCoroados = 0.80

def C_pf(larguraDeFace, diametroPrimitivo):
    F = larguraDeFace
    d = diametroPrimitivo
    if (F <= 1):
        return F/(10*d) - 0.025
    elif (F > 1 and F <= 17):
        return F/(10*d) - 0.0375 + 0.0125*F
    else:
        return F/(10*d) - 0.1109 + 0.0207*F - 0.000228*(F**2)

class C_pm_TIPO(Enum):
    mancaisImediatamenteAdjacentes = 1.00
    mancaisNaoAdjacentes = 1.10

class C_ma_TIPO(Enum):
    engrenamentoAberto = 0
    fechadasComerciais = 1
    fechadasDePrecisao = 2
    fechadasExtraprecisas = 3

def C_ma(C_ma_TIPO, larguraDeFace):
    F = larguraDeFace
    if (C_ma_TIPO.value == 0):
        A, B, C = 0.247, 0.0167, -0.765E-4
    elif (C_ma_TIPO.value == 1):
        A, B, C = 0.127, 0.0158, -0.930E-4
    elif (C_ma_TIPO.value == 2):
        A, B, C = 0.0675, 0.0128, -0.926E-4
    elif (C_ma_TIPO.value == 3):
        A, B, C = 0.00360, 0.0102, -0.822E-4
    return A + B*F + C*(F**2)

class C_e_TIPO(Enum):
    engrenamentoAjustado = 0.80
    outrasCondicoes = 1.00

def fatorDistribuicaoCarga(C_mc, C_pf, C_pm, C_ma, C_e):
    return 1 + C_mc*(C_pf*C_pm + C_ma*C_e)
