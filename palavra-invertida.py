'''
Inverte palavras digitadas pelo usuário

1. Solicitar palavra
2. Ler palavra
3. Criar variável vazia
4. Contar + 1 para cada letra da lista
5. Exibir lista com letras do maior para o menor

'''

palavra = input("Digite a palavra aqui: ")

palavra_invertida = ""

for letra in palavra:
    palavra_invertida = letra + palavra_invertida 

print(f"A palavra '{palavra}' invertida é:  {palavra_invertida}.")