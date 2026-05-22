'''
Calcular desempeho de aluno

1. Solicitar nota
2. Ler nota
3. Se a nota for maior ou igual a 7 = aprovado
4. Se não, se nota for maior ou igual a 5 = recuperação
5. Se não = reprovado
'''

nota = float(input("Digite sua nota: "))

if nota >= 7:
    print("Parabéns! Você foi aprovado.")

elif nota >= 5:
    print("Você está de recuperação.")

else:
    print("Você está reprovado.")