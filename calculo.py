def calcular_itens(convidados, carne_padrao=0.35, bebida_padrao=0.3):
    carne_necessaria = convidados * carne_padrao
    bebida_necessaria = convidados * bebida_padrao
    return carne_necessaria, bebida_necessaria
