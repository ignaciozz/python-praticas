'''
Calcular a média de três notas

1. Solicitar nota 1
2. Ler nota 1
3. Solicitar nota 2
4. Ler nota 2
5. Solicitar nota 3
6. Ler nota 3
7. Calcular média das notas 1, 2 e 3
8. Mostrar a média na tela

'''

print("Descubra qual a média das notas.")

nota1 = float(input("Digite a primeira nota: "))

nota2 = float(input("Digite a segunda nota: "))

nota3 = float(input("Digite a terceira nota: "))

soma = nota1 + nota2 + nota3
media = soma / 3

print(f"Essa é a média: {media:.1f}")