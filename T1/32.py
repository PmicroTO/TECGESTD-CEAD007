def jogo(time1, time2, gols1, gols2):
    if gols1 > gols2:
        print("O vencedor é o time " + time1)
    elif gols2 > gols1:
        print("O vencedor é o time " + time2)
    else:
        print("EMPATE")


A = input("Nome do time da casa: ")
B = input("Nome do time adversário: ")
C = input("Números de gols, time casa: ")
D = input("Números de gols, timem adversário: ")

jogo(A, B, C, D)