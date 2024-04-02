def somar_ate_cem():
    """
    Soma todos os números de 1 a 100 e printa o resultado.
    """
    soma = 0
    numero = 1
    
    while numero <= 100:
        soma += numero
        numero += 1
    
    print("A soma dos números de 1 a 100 é:", soma)

# Chama a função para somar e printar o resultado
somar_ate_cem()
