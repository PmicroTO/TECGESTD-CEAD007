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
