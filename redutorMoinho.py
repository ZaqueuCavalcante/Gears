"""Projete um engrazamento redutor de velocidade de engranagens sem-fim de **15 hp**,
com relação de redução de **13:1**, para o alimentador de um moinho de madeira serrada
usado diariamente de **3 a 10 horas**.
Um motor de indução com rotor de gaiola de **1200 rev/min** aciona o alimentador do
moinho (**K_a = 1.25**), à temperatura ambiente de **70 °F**."""

from math import pi

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
# Decisões a priori

# Função:
H_0 = 15   # [hp] - Potência de entrada.
n_W = 1200   # [rev/min] - Velocidade angular do pinhão.
m_G = 13   # [] - Razão de velocidades.
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
p_x = 1.5   # [in] - 
P_t = pi/p_x   # [] - Passo diametral tangencial.
D = N_G/P_t   # [] - 
a = 0.3183*p_x   # [in] - Adendo.
b = 0.3683*p_x   # [in] - Dedendo.
h_t = 0.6866*p_x   # [in] - Profundidade completa.

# 2 - Escolha um diâmetro médio para o pinhão:
d = 2.5   # [in] - Passo diametral.
C = (D+d)/2   # [in] - Diâmetro médio.
d_min = (1/3)*(C**0.875)   # [in] - Passo diametral mínimo.
d_max = (1/1.6)*(C**0.875)   # [in] - Passo diametral máximo.

# Largura de face da coroa:
F_G = 1

# Área lateral da carcaça:
A = 1

print("FIM")