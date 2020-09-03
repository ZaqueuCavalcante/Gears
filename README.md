# Gears

Gear design lib.
D3 Vizualization:
    - https://observablehq.com/@mbostock/epicyclic-gearing
    - https://github.com/liabru/gears-d3-js

Criar função geral para converter de in <-> mm;

# 13 - Gears-General
Características gerais das engrenagens:
    - Geometria;
    - Relações cinemáticas;
    - Forças e momentos transmitidos;
    - Tensão, resistência, segurança e confiabilidade;

## 13.1 - Types of Gears
- Cilíndricas;
- Helicoidais;
- Cônicas;
- Sem-fim;

## 13.2 - Nomenclature
- Para engrenagens cilíndricas de dentes retos:
    - Atributos fundamentais:
        - Número de dentes (N);
        - Diâmetro primitivo (d) [in ou mm];
    - Atributos derivados:
        - Módulo (m = d/N) [mm];
        - Passo diametral (P = N/d);
        - Passo circular (p = PI*d/N);

## 13.3 - Conjugate Action
- Analogia com Came;
- Perfil de **Involuta**;
- Razão de velocidade angular constante;

## 13.4 - Involute Properties
- Como gerar uma curva involuta?

## 13.5 - Fundamentals
- Como desenhar os dentes de um par de engrenagens engrazadas?
    - Grandezas fundamentais e restrições geométricas;
    - Círculos;
    - Centros;
    - Pontos tangentes;
    - Retas normais;
    - Adoçamento;

## 13.6 - Contact Ratio
- Mais de um par de dentes em contato;
- Razão de contato (m_c = q_t/p);

## 13.7 - Interference
- Ocorre quando o contato entre os dentes é feito em pontos que não pertencem a envoluta;
- Determinar qual o menor número de dentes possível para que não ocorra interferência;

## 13.8 - The Forming of Gear Teeth
- Fresagem;
- Geração;
- Caracol de Corte;
- Acabamento;

## 13.9 - Straight Bevel Gears
- Terminologia:
    - Ângulos primitivos:
        - Pinhão;
        - Coroa;

## 13.10 - Parallel Helical Gears
- Involuta Helicoidal;
- Ângulo de Hélice;
- Determinar qual o menor número de dentes possível para que não ocorra interferência;

## 13.11 - Worm Gears
- Passos axial e circular;
- Avanços;

## 13.12 - Tooth Systems
- Padrões para possibilitar a **intercambialidade** entre engrenagens:
    - Quaisquer número de dentes;
    - Mesmo ângulo de pressão;
    - Mesmo passo;

## 13.13 - Gear Trains
- Valor de trem;
- Trens planetários ou epicíclicos;

## 13.14 - Force Analysis - Spur Gearing
## 13.15 - Force Analysis - Bevel Gearing
## 13.16 - Force Analysis - Helical Gearing
## 13.17 - Force Analysis - Worm Gearing


# 14 - Spur and Helical Gears
## 14.1 - The Lewis Bending Equation
## 14.2 - Surface Durability
## 14.3 - AGMA Stress Equations
## 14.4 - AGMA Strength Equations
## 14.5 - Geometry Factors *I* and *J* (Zi and Yj)
## 14.6 - The Elastic Coefficient Cp (Ze)
## 14.7 - Dynamic Factor Kv
## 14.8 - Overload Factor Ko
## 14.9 - Surface Condition Factor Cf (Zr)
## 14.10 - Size Factor Ks
## 14.11 - Load-Distribution Factor Km (Kh)
## 14.12 - Hardness-Ratio Factor Ch (Zw)
## 14.13 - Stress-Cycle Factors Yn and Zn
## 14.14 - Reliability Factor Kr (Zy)
## 14.15 - Temperature Factor Kt (Yo)
## 14.16 - Rim-Thickness Factor Kb
## 14.17 - Safety Factors Sf and Sh
## 14.18 - Analysis
## 14.19 - Design of a Gear Mesh

# 15 - Bevel and Worm Gears
## 15.1 - Bevel Gearing - Gen
## 15.2 - Bevel-Gear Stresses and Strengths
## 15.3 - AGMA Equation Factors
## 15.4 - Straight-Bevel Gear Analysis
## 15.5 - Design of a Straight-Bevel Gear Mesh
## 15.6 - Worm Gearing - AGMA Equation
## 15.7 - Worm-Gear Analysis
## 15.8 - Designing a Worm-Gear Mesh
## 15.9 - Buckingham Wear Load
