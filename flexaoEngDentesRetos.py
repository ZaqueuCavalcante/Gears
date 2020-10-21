# Baseado na figura 14-17, do Shigley.
# Dados retirados do exemplo 14-4.

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
# Análise cinemática e dinâmica:

P_d = 10   # [dentes/in] - Passo diametral.

N_P = 17   # [dentes] - Número de dentes do pinhão.
d_P = N_P/P_d   # [in] - Diâmetro primitivo do pinhão.

N_G = 52   # [dentes] - Número de dentes da coroa.
d_G = N_G/P_d   # [in] - Diâmetro primitivo da coroa.

from math import pi, sqrt
n_P = 1800   # [rev/min] - Velocidade angular do pinhão.
V = (pi*d_P*n_P)/12   # [ft/min] - Velocidade linear no contato entre pinhão e coroa.

H = 4   # [hp] - Potência transmitida do pinhão para a coroa.
W_t = 33000*H/V   # [lbf] - Força tangencial no contato entre pinhão e coroa.

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
# Cálculo da tensão de flexão:

K_o = 1.00   # [] - Fator de sobrecarga, considerando carregamento uniforme. (Tabela pág 750)

Q_v = 6   # [] - Número de qualidade. De 3 a 7 inclue a maior parte das engrenagens comerciais.
B = 0.25 * (12-Q_v)**(2/3)   # [] - Parâmetro auxiliar.
A = 50 + 56*(1-B)   # [] - Parâmetro auxiliar.
K_v = ( (A + sqrt(V)) / A ) ** B   # [] - Fator dinâmico.

from fatorFormaLewis import fatorFormaLewis
Y_P = fatorFormaLewis(N_P)   # [] - Para o pinhão.
Y_G = fatorFormaLewis(N_G)   # [] - Para a coroa.
F = 1.5   # [in] - Largura de face.

from fatorTamanho import fatorTamanho
K_s_P = fatorTamanho(F, Y_P, P_d)   # [] - Para o pinhão.
K_s_G = fatorTamanho(F, Y_G, P_d)   # [] - Para a coroa.

import fatorDistribuicaoCarga as FDC
C_mc = FDC.C_mc_TIPO.dentesNaoCoroados.value
C_pf = FDC.C_pf(F, d_P)
C_pm = FDC.C_pm_TIPO.mancaisImediatamenteAdjacentes.value
C_ma = FDC.C_ma(FDC.C_ma_TIPO.fechadasComerciais, F)
C_e = FDC.C_e_TIPO.outrasCondicoes.value
K_m = FDC.fatorDistribuicaoCarga(C_mc, C_pf, C_pm, C_ma, C_e)   # [] - Fator de distribuição de carga.


