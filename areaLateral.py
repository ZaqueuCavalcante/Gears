def areaMinimaAGMA(C: float):
    return 43.20*C**1.7

def areaEstimada(d, D, folga):
    altura = d + D + folga
    largura = D + folga
    espessura = d + folga
    area = 2*altura*(largura + espessura) + largura*espessura
    return [altura, largura, espessura, area]
