'''
Contar vogais em uma frase

1. Solicitar frase
2. Ler frase
3. vogal = A, E, I, O, U
4. contador = 0 
5. Para LETRA em FRASE
6. Se letra = vogal
7. Somar contador + 1

'''
print("Contador de vogais.")

frase = input("Digite sua frase: ")
frase_minuscula = frase.lower()

vogal = ("a", "e", "i", "o", "u")

contador = 0

for letra in frase_minuscula:
    if letra in vogal:
        contador = contador + 1

print(f"Existem {contador} vogais na frase '{frase}'.")