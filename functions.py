import math

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
def getDiametralPitch(numberOfTeeths, pitchDiameter):
    return numberOfTeeths/pitchDiameter

def getModule(numberOfTeeths, pitchDiameter):
    return pitchDiameter/numberOfTeeths

def getCircularPitch(numberOfTeeths, pitchDiameter):
    return math.pi*pitchDiameter/numberOfTeeths

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
def getNp(k, phi):
    """ ** Valid only for a spur pair of gears, with one-to-one gear ratio **
        >> k = 1.0, for full-depth teeth
        >> k = 0.8, for stub teeth
        >> phi -> pressure angle [°]
        << output -> pinion smallest number of teeth without interference
    """
    phi = phi*math.pi/180
    aux = 3*((math.sin(phi))**2)
    return (2*k / aux) * (1 + math.sqrt(1 + aux))

def getNp(k, phi, m):
    """ ** Valid only for a spur pair of gears, with one-to-one gear ratio **
        ** and if the mating gear has more teeth than the pinion (m > 1) **
        >> k = 1.0, for full-depth teeth
        >> k = 0.8, for stub teeth
        >> phi -> pressure angle [°]
        >> m -> Ng/Np
        << output -> pinion smallest number of teeth without interference
    """
    phi = phi*math.pi/180
    aux = (1 + 2*m)*((math.sin(phi))**2)
    return (2*k / aux) * (m + math.sqrt(m**2 + aux))

def getNg(k, phi, Np):
    """ ** Valid only for a spur pair of gears, with one-to-one gear ratio **
        >> k = 1.0, for full-depth teeth
        >> k = 0.8, for stub teeth
        >> phi -> pressure angle [°]
        >> Np -> pinion number of teeth
        << output -> largest gear number of teeth with a specified pinion that is interference-free
    """
    phi = phi*math.pi/180
    aux = (math.sin(phi))**2
    return ((Np**2)*aux - 4*(k**2)) / (4*k - 2*Np*aux)

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
def getNpPinionRack(k, phi):
    """ ** Valid only for a spur pair of gears, with one-to-one gear ratio **
        >> k = 1.0, for full-depth teeth
        >> k = 0.8, for stub teeth
        >> phi -> pressure angle [°]
        << output -> smallest spur pinion that will operate with a rack without interference
    """
    phi = phi*math.pi/180
    return 2*k / (math.sin(phi))**2
    
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #

