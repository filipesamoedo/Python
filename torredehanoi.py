# Funções recursivas na prática
# Torres de Hanói
# 3 Funções. Define-se as três funções, e depois o programa principal chama as funções.

def mover_disco(origem, destino): # 1ª Função = Mover o disco de uma torre para outra.
    disco = origem.pop() # Sumir da origem
    destino.append(disco) # Aparecer no destino

def imprimir_torres(torre_A, torre_B, torre_C): # 2ª Função = Imprimir o status atual do que foi feito. Passo a passo.
    print("A:", torre_A)
    print("B:", torre_B)
    print("C:", torre_C)
    print() # Espaço em branco para manter a visualização organizada.

def torres_de_hanoi_recursivo(num_discos, origem, destino, auxiliar): # 3ª Função = Recursiva que chama a si mesma.
    if num_discos == 1:
        mover_disco(origem, destino)
        imprimir_torres(torre_A, torre_B, torre_C) # Encerra-se o jogo com apenas um passo. OU Passo final. Encerra-se também a recursiva que vai diminuindo o valor de num_discos.
    else:
        torres_de_hanoi_recursivo(num_discos - 1, origem, auxiliar, destino)
        mover_disco(origem, destino)
        imprimir_torres(torre_A, torre_B, torre_C)
        torres_de_hanoi_recursivo(num_discos - 1, auxiliar, destino, origem)

# Resolvendo o problema recursivamente. PROGRAMA PRINCIPAL

num_disco = 3
# Inicializando as torres e os discos
torre_A = list(range(num_disco, 0, -1))
torre_B = []
torre_C = []
# Mostrando o estado inicial
imprimir_torres(torre_A, torre_B, torre_C)
torres_de_hanoi_recursivo( num_disco, torre_A, torre_C, torre_B)
