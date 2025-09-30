# Criação de programa em Python. Entrada de dados do usuário
# Verificação de maior idade
# Verificação de estatura
# Verificação de Semestres concluídos
# Verificação de Idade do usuário quando se formar

#Entrada de Dados com float para idade, já que idade poderá ser somada com número decimal.

nome = input('Digite seu nome:')
idade = float(input('Digite sua idade:'))
altura = input('Digite sua altura:')
semestres = input('Digite em que semestre você esta:')

# Exibição simples de dados

print('Nome:', nome)
print('Idade:', idade)
print('Altura:', altura)
print('Semestres:', semestres)

# Detalhamento de infomações com IF
# Maior ou Menor Idade
if idade >= 18:
    print(nome, 'você é maior de idade.')
else:
    print(nome, 'você é menor de idade.')

# Estatura média, baixo ou alto

if altura >= '1.6' and altura <= '1.7':
    print('Sua estatura é mediana.')
elif altura < '1.6':
    print('Você é um baixinho fofinho.')
else:
    print('Mano, você é alto!')

# Semestres da Faculdade, quantos faltam para se formar


if semestres == '0':
    print('Ou você já se formou e meus parabéns!')
    print('Ou você ainda não esta na faculdade.')
    print('Busque sempre fazer o que você ama.')
elif semestres == '1':
    print('Parabéns por decidir estudar. Se mantenha focado!')
    print('Falta esse e + 7 semestres para você se formar')
elif semestres == '2':
    print('Parabéns por decidir estudar. Se mantenha focado!')
    print('Falta esse e + 6 semestres para você se formar')
elif semestres == '3':
    print('Parabéns por decidir estudar. Se mantenha focado!')
    print('Falta esse e + 5 semestres para você se formar')
elif semestres == '4':
    print('Parabéns por decidir estudar. Se mantenha focado!')
    print('Falta esse e + 4 semestres para você se formar')
elif semestres == '5':
    print('Parabéns por decidir estudar. Se mantenha focado!')
    print('Falta esse e + 3 semestres para você se formar')
elif semestres == '6':
    print('Parabéns por decidir estudar. Se mantenha focado!')
    print('Falta esse e + 2 semestres para você se formar')
elif semestres == '7':
    print('Parabéns por decidir estudar. Se mantenha focado!')
    print('Falta esse e + 1 semestres para você se formar')
else:
    print('Parabéns por pela dedicação. Se mantenha focado!')
    print('Falta somente esse semestre para você se formar')

# Com quantos anos em média a pessoa vai se formar

if semestres == '0':
    print('Você já se formou: Parabéns!')
    print('Ou você ainda não esta na faculdade.')
    print('Busque sempre fazer o que você ama.')
elif semestres == '1':
    print('Você se formará com', idade + 4, 'anos')
elif semestres == '2':
    print('Você se formará com', idade + 3.5, 'anos') 
elif semestres == '3':
    print('Você se formará com', idade + 3, 'anos')
elif semestres == '4':
    print('Você se formará com', idade + 2.5, 'anos')
elif semestres == '5':
    print('Você se formará com', idade + 2, 'anos')
elif semestres == '6':
    print('Você se formará com', idade + 1.5, 'anos')
elif semestres == '7':
    print('Você se formará com', idade + 1, 'anos')
else:
    print('Você se formará com', idade + 0.5, 'anos')







    
    
