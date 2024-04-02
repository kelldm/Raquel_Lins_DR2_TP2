import random
from collections import Counter

def simular_lancamento_dados(n, lados=6):
    """
    Simula o lançamento de um dado n vezes.
    n: O número de vezes que o dado será lançado.
    lados: O número de lados do dado (padrão é 6 para um dado comum de seis faces).
    Returna uma lista contendo os resultados de cada lançamento.
    """
    resultados = [random.randint(1, lados) for _ in range(n)]
    return resultados

def calcular_media(resultados):
    """
    Calcula a média dos resultados de lançamento de dados.
    resultados: Uma lista contendo os resultados de lançamento de dados.
    Returna a média dos resultados.
    """
    return sum(resultados) / len(resultados)

def calcular_distribuicao_frequencia(resultados):
    """
    Calcula a distribuição de frequência dos resultados de lançamento de dados.
    resultados: Uma lista contendo os resultados de lançamento de dados.
    Um dicionário contendo a contagem de cada elemento na lista.
    """
    return dict(Counter(resultados))

num_lancamentos = int(input("Quantas vezes deseja lançar o dado? "))

# Simula o lançamento do dado
resultados_lancamentos = simular_lancamento_dados(num_lancamentos)

# Calcula a média dos resultados
media = calcular_media(resultados_lancamentos)

# Calcula a distribuição de frequência dos resultados
distribuicao_frequencia = calcular_distribuicao_frequencia(resultados_lancamentos)
print("Resultados dos lançamentos:", resultados_lancamentos)
print("Média dos resultados:", media)
print("Distribuição de frequência dos resultados:")
for resultado, frequencia in distribuicao_frequencia.items():
    print(f"Resultado {resultado}: {frequencia} vezes")
