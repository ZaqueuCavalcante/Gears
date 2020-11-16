from math import sin, cos, radians, pi

def potenciaTransmitida(d, n, W_t):
    return (pi*d*n*W_t) / (12*33000)

def forcaDeAtrito(f, W_t_G, lambda_avanco, phi_n):
    cos_phi = cos(radians(phi_n))
    sin_lambda = sin(radians(lambda_avanco))
    cos_lambda = cos(radians(lambda_avanco))
    return (f*W_t_G) / (f*sin_lambda - cos_phi*cos_lambda)

def potenciaDeAtrito(W_f, V_S):
    return (abs(W_f)*V_S) / (33000)
