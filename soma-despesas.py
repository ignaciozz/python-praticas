despesas = 0

valor = int(input("Digite o valor da despesa: "))

while valor != 0:
    despesas = despesas + valor
    valor = int(input("Digite outro valor: "))

print(f"O total de despesas é: R$ {despesas}")