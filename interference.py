import math

# In all functions:
# >> k = 1.0, for full-depth teeth
# >> k = 0.8, for stub teeth
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
def spurGetNp(k, phi):
    """ ** Valid only for a spur pair of gears, with one-to-one gear ratio **
        >> phi -> pressure angle [°]
        << output -> pinion smallest number of teeth without interference
    """
    phi = math.radians(phi)
    aux = 3*((math.sin(phi))**2)
    return (2*k / aux) * (1 + math.sqrt(1 + aux))

def spurGetNp(k, phi, m):
    """ ** Valid only for a spur pair of gears, with one-to-one gear ratio **
        ** and if the mating gear has more teeth than the pinion (m > 1) **
        >> phi -> pressure angle [°]
        >> m -> Ng/Np
        << output -> pinion smallest number of teeth without interference
    """
    phi = math.radians(phi)
    aux = (1 + 2*m)*((math.sin(phi))**2)
    return (2*k / aux) * (m + math.sqrt(m**2 + aux))

def spurGetNg(k, phi, Np):
    """ ** Valid only for a spur pair of gears, with one-to-one gear ratio **
        >> phi -> pressure angle [°]
        >> Np -> pinion number of teeth
        << output -> largest gear number of teeth with a specified pinion that is interference-free
    """
    phi = math.radians(phi)
    aux = (math.sin(phi))**2
    return ((Np**2)*aux - 4*(k**2)) / (4*k - 2*Np*aux)

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
def pinionRackGetNp(k, phi):
    """ ** Valid only for a spur pair of gears, with one-to-one gear ratio **
        >> phi -> pressure angle [°]
        << output -> smallest spur pinion that will operate with a rack without interference
    """
    phi = math.radians(phi)
    return 2*k / (math.sin(phi))**2
    
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
def helicalGetNp(k, phi, psi, m):
    """ ** Valid only for a helical pair of gears **
        >> phi -> pressure angle [°]
        >> psi -> some angle [°]
        >> m -> Ng/Np
        << output -> smallest helical pinion teeth number without interference
    """
    phi = math.radians(phi)
    psi = math.radians(psi)
    aux = (1 + 2*m)*((math.sin(phi))**2)
    return (2*k*math.cos(psi) / aux) * (m + math.sqrt(m**2 + aux))

def helicalGetNg(k, phi, psi, Np):
    """ ** Valid only for a helical pair of gears **
        >> phi -> pressure angle [°]
        >> psi -> some angle [°]
        >> Np -> pinion number of teeth
        << output -> largest gear number of teeth with a specified pinion that is interference-free
    """
    sin = math.sin(math.radians(phi))
    cos = math.cos(math.radians(psi))
    up = (Np*sin)**2 - 4*(k*cos)**2
    down = 4*k*cos - 2*Np*(sin**2)
    return up/down
