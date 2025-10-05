# Quando a função não retorna nada ela é considerada um procedimento.
# Parâmetro é quando vc passa um valor para um função.
# Parâmetros, procedimentos e funções

def func1(x):
    x = 10
    print(f'Função func1 - x = {x}')

def func2(x):
    x = 20
    print(f'Função func2 - x = {x}')
    return x

vn = 0
print(f'Programa principal - vn = {vn}')
vn = func1(vn)
print(f'Programa principal - vn = {vn}')
vn = func2(vn)
print(f'Programa principal - x = {vn}')

# Exemplo 2. Remoção do RETURN e subtituição de vn por x

def func1(x):
    x = 10
    print(f'Função func1 - x = {x}')

def func2(x):
    x = 20
    print(f'Função func2 - x = {x}')

x = 0
print(f'Programa principal - x = {x}')
vn = func1(vn)
print(f'Programa principal - x = {x}')
vn = func2(vn)
print(f'Programa principal - x = {x}')

# Por que o resultado muda de None para X? Antes modificava-se o VN e retornava da função.
# Agora o X no contexto é 0.

# Exemplo 3

def func1():
    global x
    x = 10
    print(f'Função func1 - x = {x}')

def func2():
    global x
    x = 20
    print(f'Função func2 - x = {x}')

# O uso de GLOBAL funciona como se fosse um return.
# Pois altera o valor da variável no código/programa principal.

# Último exemplo

def taximetro(distancia):
    def calculaMult():
        if distancia < 5:
            return 1.2
        else:
            return 1

    multiplicador = calculaMult()
    largada = 3
    km_rodado = 2
    valor = (largada + distancia * km_rodado) * multiplicador
    return valor

dist = eval(input("Entre com a distância a ser percorrida em km: "))
pagamento = taximetro(dist)
print(f'O valor a pagar é R$ {pagamento}')
