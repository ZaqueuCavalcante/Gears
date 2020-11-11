"""Projete um engrazamento redutor de velocidade de engranagens sem-fim de **10 hp**,
com relação de redução de **11:1**, para o alimentador de uma plaina de marcenaria
usada diariamente de **3 a 10 horas**.
Um motor de indução com rotor de gaiola de esquilo de **1720 rev/min** aciona o 
alimentador da plaina (**K_a = 1.25**), à temperatura ambiente de **70 °F**."""

from math import pi, atan, cos, tan, radians, sin

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
# Decisões a priori

# Função:
H_0 = 10   # [hp] - Potência de entrada.
n_W = 1720   # [rev/min] - Velocidade angular do pinhão.
m_G = 11   # [] - Razão de velocidades.
K_a = 1.25   # [] - 

# Fator de projeto:
n_d = 1.2   # [] - Fator de projeto.

# Materiais e processos:
materialPinhao = "aço-liga endurecido superficialmente"
materialCoroa = "bronze fundida em areia"

# Número de roscas no pinhão:
# [14.5, 17.5, 20, 22.5, 25, 27.5, 30]
phi_n = 20   # [°] - Ângulo de pressão normal.
N_W = 2   # [dentes] - Número de dentes do pinhão.
from dentesCoroa import numeroDentesCoroa
N_G = numeroDentesCoroa(m_G, N_W, phi_n)   # [dentes] - Número de dentes da coroa.

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
# Decisões de projeto

# 1 - Escolha um passo axial para a coroa:
p_x = 1.5   # [in] - Passo axial da coroa.
P_t = pi/p_x   # [] - Passo diametral tangencial.
D = N_G/P_t   # [] - Diâmetro médio da coroa.
a = 0.3183*p_x   # [in] - Adendo.
b = 0.3683*p_x   # [in] - Dedendo.
h_t = 0.6866*p_x   # [in] - Profundidade completa.

# 2 - Escolha um diâmetro médio para o pinhão:
d = 2.5   # [in] - Passo diametral.
C = (D+d)/2   # [in] - Diâmetro médio.
d_min = (1/3)*(C**0.875)   # [in] - Passo diametral mínimo.
d_max = (1/1.6)*(C**0.875)   # [in] - Passo diametral máximo.

import anguloAvanco as AA
L = p_x*N_W   # [in] - Avanço do parafuso sem-fim.
lambda_avanco = AA.anguloAvanco(L, d, phi_n)   # [°] - Ângulo de avanço.

import velocidades as VLC
V_S = VLC.velocidadeDeslizamentoPinhao(d, n_W, lambda_avanco)   # [ft/min] - Velocidade de deslizamento do pinhão.
V_W = VLC.velocidadeLinear(d, n_W)   # [ft/min] - Velocidade linear do pinhão.
n_G = VLC.velocidadeAngular(n_W, m_G)   # [rev/min] - Velocidade angular da coroa.
V_G = VLC.velocidadeLinear(D, n_G)   # [ft/min] - Velocidade linear do pinhão.

# Fator dos materiais
import fatorMateriais as FM
tipoFundicaoCoroa = FM.Fundicao.areia
C_S = FM.fatorMateriais(C, D, tipoFundicaoCoroa)

# Fator de correção da razão de engrenamento
import fatorCorrecaoRazao as FCR
C_m = FCR.fatorCorrecaoRazao(m_G)   # [] - Fator de correção da razão de engrenamento.

# Fator de velocidade
import fatorVelocidade as FV
C_v = FV.fatorVelocidade(V_S)   # [] - Fator de velocidade.

# Coeficiente de atrito
import coeficienteAtrito as CA
f = CA.coeficienteAtrito(V_S)   # [] - Coeficiente de atrito.

# Eficiência mecânica, quando o pinhão conduz o conjunto de engrenagens
import eficienciaMecanica as EM
e = EM.eficienciaMecanica(phi_n, lambda_avanco, f, EM.Condutor.pinhao)

# Componente tangencial da força nas engrenagens:
W_t_G = (33000*n_d*H_0*K_a)/(V_G*e)
cos_phi = cos(radians(phi_n))
sin_lambda = sin(lambda_avanco)
cos_lambda = cos(lambda_avanco)
W_t_W = W_t_G * (cos_phi*sin_lambda + f*cos_lambda) / (cos_phi*cos_lambda - f*sin_lambda)

# Potencias transmitidas pelas engrenagens:
H_W = (pi*d*n_W*W_t_W) / (12*33000)   # [hp] - Potência transmitida pelo pinhão.
H_G = (pi*D*n_G*W_t_G) / (12*33000)   # [hp] - Potência transmitida pela coroa.

W_f = (f*W_t_G) / (f*sin_lambda - cos_phi*cos_lambda)
H_f = (abs(W_f)*V_S) / (33000)   # [hp] - Potência de atrito.

# 3 - Valor de F_e_G:
F_e_min = (W_t_G) / (C_S*(D**0.8)*C_m*C_v)   # [in] - 
F_e_max = 2*d/3   # [in] - 
F_e_G = 1.5   # [in] - 

W_t_adm = C_S*(D**0.8)*F_e_G*C_m*C_v   # [lbf] - 

# 4 - Análise térmica:
import eficienciaTermica as ET
h_CR = ET.eficienciaTermicaGeral(n_W, ET.Eixo.semVentilador)   # [ft.lbf/(min.in².°F)] - 
H_perda = 33000*(1-e)*H_W   # [ft.lbf/min] - 

A_min = 43.20*C**1.7   # [in²] - Área lateral mínima (AGMA).
A = 1100   # [in²] - Área lateral da carcaça escolhida.

t_a = 70   # [°F] - Temperatura ambiente.
t_s = t_a + H_perda/(h_CR*A)   # [°F] - Temperatura do reservatório de óleo.

P_n = P_t/cos_lambda
p_n = pi/P_n

import fatorFormaLewis as FFL
y = FFL.fatorFormaLewis(phi_n)

sigma_flexao_coroa = W_t_G/(p_n*F_e_G*y)   # [psi] - 

print("FIM")
