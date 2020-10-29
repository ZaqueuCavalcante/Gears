from math import pi, sqrt, sin, radians, ceil, floor

# Em todas as funções:
# >> k = 1.0, para dentes de altura completa.
# >> k = 0.8, para dentes diminuídos.
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
def Np(k, phi, m_G):
    phi = radians(phi)
    if (m_G <= 1):
        aux = 3*((sin(phi))**2)
        return ceil( (2*k / aux) * (1 + sqrt(1 + aux)) )
    else:
        aux = (1 + 2*m_G)*((sin(phi))**2)
        return ceil ( (2*k / aux) * (m_G + sqrt(m_G**2 + aux)) )

def Ng(k, phi, Np):
    phi = radians(phi)
    aux = (sin(phi))**2
    #return floor( ((Np**2)*aux - 4*(k**2)) / (4*k - 2*Np*aux) )
    return ((Np**2)*aux - 4*(k**2)) / (4*k - 2*Np*aux)
