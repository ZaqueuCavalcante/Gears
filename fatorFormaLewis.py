phi_n_values = [14.5, 20, 25, 30]
y_values = [0.100, 0.125, 0.150, 0.175]

def fatorFormaLewis(phi_n: float):
    if (phi_n in phi_n_values):
        index = phi_n_values.index(phi_n)
        return y_values[index]  
    else:
        return "phi_n inválido."
