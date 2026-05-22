'''
Contador de letras em uma palavra

1. Solicitar palavra
2. Ler palavra
3. Criar contador com início 0
4. Para cada letra, somar contador +1
5. Retornar soma 

'''
print("Veja quantas letras sua palavra tem.")

palavra = input("Digite a palavra aqui: ") 

contador = (0)

for letra in palavra:
    contador = contador + 1

print(f"A palavra '{palavra}' possui {contador} letras.")