# Atividade 3
# Escreva uma função que busca de forma iterativa o maior elemento em uma lista de números inteiros.

lista = (555,60,98,75,42,15,3500)

maior = lista[0]

for i in range (len(lista)): # len(lista) entrega a quantidade de itens dentro da lista. Evita erros.
    if lista[i] > maior:
        maior = lista[i]
    
print('O maior número é:', maior)

# Versão mais elegante. Definindo Função.

def encontrar_maior_elemento_iterativo(lista):
  """
  Encontra o maior elemento em uma lista de números inteiros de forma não recursiva.

  Args:
    lista: A lista de números inteiros.

  Returns:
    O maior elemento da lista.
  """

  if len(lista) <= 1:
    # Caso base: se a lista tiver no máximo 1 elemento, ele é o maior
    return lista[0]

  maior_elemento = lista[0]
  for numero in lista[1:]:  # Dessa forma o programa acessa diretamente OS VALORES. Não OS ÍNDICES. Maior eficiencia, pois começa do segundo elemento.
    if numero > maior_elemento:
      maior_elemento = numero

  return maior_elemento

# Exemplo de uso
lista_exemplo = [7, 2, 5, 1, 4, 3, 6]
maior_elemento = encontrar_maior_elemento_iterativo(lista_exemplo)
print(f"O maior elemento da lista é: {maior_elemento}")

""" Apesar de ser uma versão mais elegante ela não otimiza o uso do processador.

A versão com índices é MAIS RÁPIDA!
Por quê?
lista[1:] cria uma CÓPIA da lista (exceto o primeiro elemento)

Cópia consome memória e tempo

Acesso por índice é otimizado em Python ""
