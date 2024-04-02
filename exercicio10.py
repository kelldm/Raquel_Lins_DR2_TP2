def decimal_para_binario(decimal):
    """
    Converte um número da base decimal para a base binária.
    decimal: O número na base decimal a ser convertido.
    Returna o número convertido para a base binária.
    """
    if decimal == 0:
        return '0'
    
    binario = ''
    while decimal > 0:
        resto = decimal % 2
        binario = str(resto) + binario
        decimal //= 2
    
    return binario

# Exemplo de uso da função:
numero_decimal = int(input("Digite um número na base decimal: "))

numero_binario = decimal_para_binario(numero_decimal)
print("O número em binário é:", numero_binario)
