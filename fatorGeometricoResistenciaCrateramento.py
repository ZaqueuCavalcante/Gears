from math import radians, sin, cos

def fatorGeometricoResistenciaCrateramento(phi_n, m_N, m_G):
    phi_n = radians(phi_n)
    return (sin(phi_n)*cos(phi_n)/(2*m_N)) * (m_G/(m_G+1))
