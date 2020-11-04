from math import pi, sin, cos, sqrt, radians

def razaoCompartilhamentoCarga(phi_n, phi_t, phi_helice, P_d, N_P, N_G):
    phi_n = radians(phi_n)
    phi_t = radians(phi_t)
    phi_helice = radians(phi_helice)

    P_N = (pi/P_d) * cos(phi_n)

    a = 1 / P_d
    r_P = N_P/(2*cos(phi_helice))
    r_b_P = r_P * cos(phi_t)
    r_G = N_G/(2*cos(phi_helice))
    r_b_G = r_G * cos(phi_t)
    Z = sqrt( (r_P + a)**2 - r_b_P**2 ) + sqrt( (r_G + a)**2 - r_b_G**2 ) - (r_P + r_G)*sin(phi_t)

    return P_N/(0.95*Z)
