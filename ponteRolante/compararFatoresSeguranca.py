def compararFatoresSeguranca(nomeEngrenagem, fatorFlexao, fatorDesgaste):
    if (fatorFlexao < fatorDesgaste**2):
        print("O risco do(a) " + nomeEngrenagem + " provém da FLEXÃO.")
    elif (fatorDesgaste**2 < fatorFlexao):
        print("O risco do(a) " + nomeEngrenagem + " provém do DESGASTE.")
    else:
        print("Os fatores de segurança do(a) " + nomeEngrenagem + " são idênticos.")
