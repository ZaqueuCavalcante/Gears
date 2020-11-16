from math import sin, cos, radians

def forcaTangencialCoroa(n_d, H_0, K_a, V_G, e):
    return (33000*n_d*H_0*K_a)/(V_G*e)

def forcaTangencialPinhao(phi_n, lambda_avanco, W_t_G, f, ):
    cos_phi = cos(radians(phi_n))
    sin_lambda = sin(radians(lambda_avanco))
    cos_lambda = cos(radians(lambda_avanco))
    return W_t_G * (cos_phi*sin_lambda + f*cos_lambda) / (cos_phi*cos_lambda - f*sin_lambda)
