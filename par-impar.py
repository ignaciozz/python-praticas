'''
Verificar se um número é par ou ímpar.

1. Pedir um número
2. Ler número
3. Verificar se é divisível por 2
4. Se sim, informar que número é par
5. Se não, informar que é ímpar 

'''

print("Quer saber se o número é par ou ímpar?")

num = int(input("Digite o número: "))

if num % 2 == 0:
    print(f"O número {num} é par.")
else:
    print(f"O número {num} é impar.")