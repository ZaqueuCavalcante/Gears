# Baseado na figura 14-17, do Shigley.
# Dados retirados do exemplo 14-4.
from math import pi, sin, cos, radians

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
# Decisões iniciais:

H = 4   # [hp] - Potência transmitida do pinhão para a coroa.
n_P = 1800   # [rev/min] - Velocidade angular do pinhão.
R = 0.90   # [] - Confiabilidade considerando carga suave.
N_CC_P = 1E8   # [ciclos] - Número de ciclos de carga para o pinhão.
K_o = 1.00   # [] - Fator de sobrecarga, considerando carregamento uniforme.

n_d = 2   # [] - Fator de projeto para exigências não quantificadas.

phi_n = 20   # [°] - Ângulo de pressão (sistema de dentes).

N_P = 17   # [dentes] - Número de dentes do pinhão.
N_G = 52   # [dentes] - Número de dentes da coroa.
# CONSIDERAR INTERFERÊNCIA P.667

Q_v = 6   # [] - Número de qualidade. De 3 a 7 inclue a maior parte das engrenagens comerciais.

P_d = 10   # [dentes/in] - Passo diametral TENTATIVO.
F = 1.5   # [in] - Largura de face/engrazamento. Recomendação: 3.pi/P_d <= F <= 5.pi/P_d

m_B = 1.30   # [] - Razão auxiliar (apenas para ser > 1.20).

K_T = 1   # [] - Fator de temperatura.
C_f = 1   # [] - Fator de condição superficial.

m_N = 1   # [] - Razão de compartilhamento de carga.

C_P = 2300   # [sqrt(psi)] - Coeficiente elástico.

H_B_P = 240   # [Brinell] - Dureza do pinhão.
H_B_G = 200   # [Brinell] - Dureza da coroa.

J_P = 0.30   # [] - Razão de Poisson para o pinhão.
J_G = 0.40   # [] - Razão de Poisson para a coroa.

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
# Análise cinemática e dinâmica:

d_P = N_P/P_d   # [in] - Diâmetro primitivo do pinhão.
d_G = N_G/P_d   # [in] - Diâmetro primitivo da coroa.

V = (pi*d_P*n_P)/12   # [ft/min] - Velocidade linear no contato entre pinhão e coroa.
W_t = 33000*H/V   # [lbf] - Força tangencial no contato entre pinhão e coroa.

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
# Cálculo da tensão de flexão:

from fatorDinamico import fatorDinamico
K_v = fatorDinamico(Q_v, V)   # [] - Fator dinâmico.

from fatorFormaLewis import fatorFormaLewis
Y_P = fatorFormaLewis(N_P)   # [] - Para o pinhão.
Y_G = fatorFormaLewis(N_G)   # [] - Para a coroa.

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

from fatorEspessuraAro import fatorEspessuraAro
K_B = fatorEspessuraAro(m_B)   # [] - Fator de espessura de aro.

import fatorCiclagemTensao as FCT
m_G = N_G/N_P    # [] - Razão de velocidades.
N_CC_G = N_CC_P/m_G   # [ciclos] - Número de ciclos de carga para a coroa.
Y_N_P = FCT.fatorCiclagemTensao(N_CC_P)   # [] - Para o pinhão.
Y_N_G = FCT.fatorCiclagemTensao(N_CC_G)   # [] - Para a coroa.

from fatorConfiabilidade import fatorConfiabilidade
K_R = fatorConfiabilidade(R)   # [] - Fator de confiabilidade.

phi_n = radians(phi_n)
I = (sin(phi_n)*cos(phi_n)/(2*m_N)) * (m_G/(m_G+1))   # [] - Fator geométrico de resistência ao crateramento.

import tensaoFlexaoAdmissivel as TFA
S_t_P = TFA.tensaoFlexaoAdmissivel(TFA.Dureza_TIPO.brinellGrau1, H_B_P)   # [psi] - Para o pinhão.
S_t_G = TFA.tensaoFlexaoAdmissivel(TFA.Dureza_TIPO.brinellGrau1, H_B_G)   # [psi] - Para a coroa.

import tensaoContatoAdmissivel as TCA
S_C_P = TCA.tensaoContatoAdmissivel(TCA.Dureza_TIPO.brinellGrau1, H_B_P)
S_C_G = TCA.tensaoContatoAdmissivel(TCA.Dureza_TIPO.brinellGrau1, H_B_G)

from fatorCiclagemTensaoCrateramento import fatorCiclagemTensaoCrateramento
Z_N_P = fatorCiclagemTensaoCrateramento(N_CC_P)   # [] - Para o pinhão.
Z_N_G = fatorCiclagemTensaoCrateramento(N_CC_G)   # [] - Para a coroa.

from fatorRazaoDureza import fatorRazaoDureza
RD = H_B_P/H_B_G   # [] - Razão de dureza.
C_H = fatorRazaoDureza(RD, m_G)   # [] - Fator de razão de dureza.

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
# Flexão dos dentes do pinhão:
sigma_P = W_t * K_o * K_v * K_s_P * (P_d/F) * (K_m*K_B/J_P)   # [psi] - Tensão nos dentes do pinhão.
S_F_P = ( (S_t_P*Y_N_P)/(K_T*K_R) ) / sigma_P   # [] - Fator de segurança sob flexão para o pinhão.

# Flexão dos dentes da coroa:
sigma_G = W_t * K_o * K_v * K_s_G * (P_d/F) * (K_m*K_B/J_G)   # [psi] - Tensão nos dentes do pinhão.
S_F_G = ( (S_t_G*Y_N_G)/(K_T*K_R) ) / sigma_G   # [] - Fator de segurança sob flexão para o pinhão.

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
# Desgaste dos dentes do pinhão:
sigma_c_P = C_P * (W_t * K_o * K_v * K_s_P * (K_m/(d_P*F)) * (C_f/I))**(1/2)   # [psi] - Tensão nos dentes do pinhão.
S_H_P = ( (S_C_P*Z_N_P)/(K_T*K_R) ) / sigma_c_P   # [] - Fator de segurança sob desgaste para o pinhão.

# Desgaste dos dentes da coroa:
sigma_c_G = (K_s_G/K_s_P)**(1/2) * sigma_c_P   # [psi] - Tensão nos dentes da coroa.
S_H_G = ( (S_C_G*Z_N_G*C_H)/(K_T*K_R) ) / sigma_c_G   # [] - Fator de segurança sob desgaste para a coroa.

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
# Fatores de segurança:
from compararFatoresSeguranca import compararFatoresSeguranca
compararFatoresSeguranca("pinhão", S_F_P, S_H_P)
compararFatoresSeguranca("coroa", S_F_G, S_H_G)
