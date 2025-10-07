# Atividade 3
# Escreva uma função que busca de forma iterativa o maior elemento em uma lista de números inteiros.

lista = (555,60,98,75,42,15,3500)

maior = lista[0]

for i in range (len(lista)): # len(lista) entrega a quantidade de itens dentro da lista. Evita erros.
    if lista[i] > maior:
        maior = lista[i]
    
print('O maior número é:', maior)
