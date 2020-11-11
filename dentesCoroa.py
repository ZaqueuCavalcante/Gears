phi_n_values = [14.5, 20, 25, 30]
N_G_min_values = [40, 21, 14, 10]

def numeroDentesCoroa(m_G: int, N_W: int, phi_n: float):
    if (phi_n in phi_n_values):
        N_G = m_G*N_W
        N_G_min = getN_W_min(phi_n)
        if (N_G < N_G_min):
            return "N_G = {} e N_G_min = {}".format(N_G, N_G_min)
        return N_G
    else:
        return "phi_n inválido."

def getN_W_min(phi_n: float):
    index = phi_n_values.index(phi_n)
    return N_G_min_values[index]
