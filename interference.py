from math import pi, sqrt, sin, radians

# Em todas as funções:
# >> k = 1.0, para dentes de profundidade completa
# >> k = 0.8, para dentes 
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
def Np(k, phi):
    phi = radians(phi)
    aux = 3*((sin(phi))**2)
    return (2*k / aux) * (1 + sqrt(1 + aux))

def Np(k, phi, m):
    phi = radians(phi)
    aux = (1 + 2*m)*((sin(phi))**2)
    return (2*k / aux) * (m + sqrt(m**2 + aux))

def Ng(k, phi, Np):
    phi = radians(phi)
    aux = (sin(phi))**2
    return ((Np**2)*aux - 4*(k**2)) / (4*k - 2*Np*aux)
