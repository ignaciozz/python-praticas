'''
Somar despesas

1. Solicitar valor
2. Ler valor
3. Enquanto valor for diferente de 0, somar valores
4. Quando valor for 0, exibir total
'''

despesas = 0

valor = int(input("Digite o valor da despesa: "))

while valor != 0:
    despesas = despesas + valor
    valor = int(input("Digite outro valor: "))

print(f"O total de despesas é: R$ {despesas}")