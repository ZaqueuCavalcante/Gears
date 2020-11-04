from math import radians, sin, cos

def fatorGeometricoResistenciaCrateramento(phi_t, m_N, m_G):
    phi_t = radians(phi_t)
    return (sin(phi_t)*cos(phi_t)/(2*m_N)) * (m_G/(m_G+1))
