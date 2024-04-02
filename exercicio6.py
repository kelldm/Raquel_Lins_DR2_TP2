def verificar_primo(numero):
    """
    Verifica se um número é primo.
    numero: O número a ser verificado.
    retorna true se o número for primo, false se nao for
    """
    if numero <= 1:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True

def listar_numeros_primos():
    """
    Lista todos os números primos entre 1 e 100
    retorna uma lista contendo todos os números primos entre 1 e 100
    """
    primos = []
    for numero in range(1, 101):
        if verificar_primo(numero):
            primos.append(numero)
    return primos

# Chama a função para listar os números primos e printa o resultado
lista_primos = listar_numeros_primos()
print("Números primos entre 1 e 100:")
print(lista_primos)
