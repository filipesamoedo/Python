# Função Recursiva versus Iterativa
# Contagem Regressiva

def regressiva (x):
    print(x)
    if x > 0:
        regressiva(x- 1)
    else:
        print('acabou')
regressiva(10)

# não recursiva
for y in range (10 ,-1, -1):
    print(y)
print('acabou')

# Como decidir?7
# Na maioria das vezes e uma questão de gosto.
# Porem em alguns casos a Recursiva é ideal

# Exemplo 2. RECURSIVA FATORIAL

def fatorial(n):
    if n == 0 or n == 1: # Fat de 0 e de 1 é 1
        return 1
    else:
        return n*fatorial(n-1)
vfat = fatorial(5)
print(f'resultado recursivo: {vfat}')

# função fatorial não recursiva

def fatorial(n):
    fat = 1
    if n == 0 or n == 1:
        return fat
    else:
        for x in range(2, n + 1):
            fat = fat*x
        return fat
vfat = fatorial(5)
print(f'resultado iterativa: {vfat}')


# docstrings
# Determina o n-ésimo termo da sequencia de fibonacci

def fibo(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)

vfibo= fibo(6)
print(vfibo)
print(help(fibo))
    
