from math import sqrt

def fatorCorrecaoRazao(m_G: int):
    if (m_G > 3 and m_G <= 20):
        return 0.02*sqrt(-m_G**2 + 40*m_G - 76) + 0.46
    if (m_G > 20 and m_G <= 76):
        return 0.0107*sqrt(-m_G**2 + 56*m_G - 5145)
    return 1.1483 - 0.00658*m_G
