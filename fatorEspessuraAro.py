from math import log

def fatorEspessuraAro(m_B):
    if (m_B < 1.2 and m_B > 0):
        return 1.6 * log(2.242/m_B)
    return 1.00
