# Figura 14-15. Como decidir qual curva utilizar?
def fatorCiclagemTensaoCrateramento(numeroCiclosCarga):
    N = numeroCiclosCarga
    return 1.4488 * N**(-0.023)
