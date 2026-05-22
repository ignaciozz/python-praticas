'''
Converter temperatura de Celsius para Fahrenheit 

1. Solicitar temperatura em Celsius
2. Ler temperatura
3. Multiplicar temperatura por 1,8
4. Somar 32 ao resultado

'''

print("Conversor de temperatura de Celsius para Fahrenheit")

celsius = float(input("Digite a temperatura em °C: "))
fahrenheit = (celsius * 1.8) + 32

print(f"{celsius:.1f} graus em Fahrenheit é: {fahrenheit:.1f}")