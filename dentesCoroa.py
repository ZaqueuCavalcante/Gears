phi_n_values = [14.5, 17.5, 20, 22.5, 25, 27.5, 30]
N_G_min_values = [40, 27, 21, 17, 14, 12, 10]

def numeroDentesCoroa(m_G, N_W, phi_n):
    if (phi_n in phi_n_values):
        N_G = m_G*N_W
        N_G_min = getN_W_min(phi_n)
        if (N_G < N_G_min):
            return "N_G = {} e N_G_min = {}".format(N_G, N_G_min)
        return N_G
    else:
        return "phi_n inválido."

def getN_W_min(phi_n):
    index = phi_n_values.index(phi_n)
    return N_G_min_values[index]
    