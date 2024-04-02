def concatenar_e_organizar(lista1, lista2):
    """
    Concatena duas listas fornecidas pelo usuário e as organiza em ordem crescente
    lista1: Primeira lista fornecida pelo usuário.
    lista2: Segunda lista fornecida pelo usuário.
    
    retorna: A lista da concatenação e em ordem crescente.
    """
    lista_concatenada = lista1 + lista2
    lista_concatenada.sort()
    return lista_concatenada

# Solicita ao usuário para fornecer duas listas
lista1 = [int(x) for x in input("Digite os números da primeira lista separados por espaço: ").split()]
lista2 = [int(x) for x in input("Digite os números da segunda lista separados por espaço: ").split()]

# Chama a função para concatenar e organizar as listas
lista_concatenada_organizada = concatenar_e_organizar(lista1, lista2)

# Printa a lista resultante
print("Lista concatenada e organizada em ordem crescente:", lista_concatenada_organizada)
