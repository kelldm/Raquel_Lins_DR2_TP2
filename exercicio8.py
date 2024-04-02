def potencia(numero, expoente=2):
    """
    Calcula a potência de um número com um expoente especifico
    numero: o número base
    expoente: o expoente 
    retorna o resultado da operação de potenciação
    """
    resultado = numero ** expoente
    return resultado

base = float(input("Digite o número base: "))
expoente = int(input("Digite o expoente (padrão é 2): "))

resultado = potencia(base, expoente)
print(f"O resultado de {base} elevado a {expoente} é:", resultado)
