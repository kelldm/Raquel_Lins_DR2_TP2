def celsius_para_fahrenheit(celsius):
    """
    Converte temperatura de Celsius para Fahrenheit.
    celsius: Valor da temperatura em graus Celsius.
    retorna o valor da temperatura convertida em graus Fahrenheit.
    """
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

temp_celsius = float(input("Digite a temperatura em Celsius: "))
temp_fahrenheit = celsius_para_fahrenheit(temp_celsius)
print("A temperatura em Fahrenheit é:", temp_fahrenheit)
