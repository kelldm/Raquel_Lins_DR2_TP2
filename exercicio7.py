def desenhar_linha(caractere='-', comprimento=30):
    """
    Desenha uma linha na tela utilizando um caractere especifico e um comprimento especifico
    caractere: O caractere a ser utilizado para desenhar a linha (padrão é '-').
    comprimento: O comprimento da linha a ser desenhada
    """
    linha = caractere * comprimento
    print(linha)

# Chamando a função sem passar argumentos
desenhar_linha()

# Chamando a função com argumentos personalizados
desenhar_linha('*', 50)
