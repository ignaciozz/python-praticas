'''
Descobrir se número é positivo, negativo ou zero

1. Solicitar número
2. Ler número
3. Verificar se número é (-), (+) ou Zero
4. Se (-) = printar "Esse número número negativo"
5. Se (+) = printar "Esse número número positivo"
6. Se Zero = printar "Esse número é Zero"

'''
print("Descubra se seu número é positivo, negativo ou zero.")

num = int(input("Digite o número: "))

if num > 0:
    print(f"O número {num} é positivo.")

elif num < 0:
    print(f"O número {num} é negativo.")

else:
    print(f"O número é zero.")
