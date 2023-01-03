# Uma empresa quer verificar se um empregado está qualificado para a aposentadoria ou não. Para
# estar em condições, um dos seguintes requisitos deve ser satisfeito:
# - Ter no mínimo 65 anos de idade.
# - Ter trabalhado no mínimo 30 anos.
# - Ter no mínimo 60 anos e ter trabalhado no mínimo 25 anos.
# Com base nas informações acima, faça um algoritmo que leia: o número do empregado (código), o ano
# de seu nascimento e o ano de seu ingresso na empresa. O programa deverá escrever a idade e o tempo
# de trabalho do empregado e a mensagem 'Requerer aposentadoria' ou 'Não requerer'.

import datetime
today = datetime.date.today()
Y = today.year

C = input("Número do empregado: ")
N = input("Ano de naascimento: ")
I = input("Ano de ingresso na empresa: ")

if (int(Y) - int(N)) >= 65:
    A = True
elif (int(Y) - int(I)) >= 30:
    A = True
elif (int(Y) - int(N)) >= 65 and (int(Y) - int(I)) >= 25:
    A = True
else:
    A = False

IDADE = int(Y) - int(N)
TEMPO = int(Y) - int(I)

if A is True:
    print("Idade: " + str(IDADE), ", Tempo de Trabalho: " +
          str(TEMPO), "Requerer aposentadoria,")
else:
    print("Idade: " + str(IDADE), ", Tempo de Trabalho: " +
          str(TEMPO), "Não requerer aposentadoria,")
