# Seção 14-12.
def fatorRazaoDureza(razaoDureza, razaoVelocidade):
    RD = razaoDureza
    m_G = razaoVelocidade
    if (RD < 1.2):
        A = 0
    elif (RD >= 1.2 and RD <= 1.7):
        A = 8.98E-3 * RD - 8.29E-3
    else:
        A = 0.00698
    return 1.00 + A*(m_G - 1.00)
