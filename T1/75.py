# Escreva um algoritmo que imprima as seguintes seqüências de números: (1, 1 2 3 4 5 6 7 8 9 10)
# (2, 1 2 3 4 5 6 7 8 9 10) (3, 1 2 3 4 5 6 7 8 9 10) (4, 1 2 3 4 5 6 7 8 9 10) e assim sucessivamente, até
# que o primeiro número (antes da vírgula), também chegue a 10.
### INCOMPLETA

def head():
    base = 0
    for x in range(1, 11):
        base += 1
        print(base, end = ", \n")


def um_a_dez():
    for y in range(1, 11):
        for x in range(1, 11):
            print(x, end = "")


def final():
    head()
    um_a_dez()


final()