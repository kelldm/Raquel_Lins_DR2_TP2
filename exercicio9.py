def calcular_fatorial(numero):
    """
    Calcula o fatorial de um número
    numero: o número para o qual calcular o fatorial
    retorna fatorial do número fornecido
    """
    if numero < 0:
        return "Erro: números negativos."
    elif numero == 0 or numero == 1:
        return 1
    else:
        fatorial = 1
        for i in range(2, numero + 1):
            fatorial *= i
        return fatorial

numero = int(input("Digite um número para calcular o fatorial: "))

resultado = calcular_fatorial(numero)
print("O fatorial de", numero, "é:", resultado)
