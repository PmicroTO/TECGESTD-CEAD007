# Ler a hora de início e a hora de fim de um jogo de Xadrez (considere apenas horas inteiras, sem os
# minutos) e calcule a duração do jogo em horas, sabendo-se que o tempo máximo de duração do jogo é
# de 24 horas e que o jogo pode iniciar em um dia e terminar no dia seguinte.
def xadrez(inicio, fim):
    HI = inicio
    HF = fim
    DUR = HF - HI
    if DUR > 0:
        print(DUR)
    else:
        print((24 - HI) + HF)


A = input("Hora inicial(FORMATO 24H): ")
B = input("Hora final(FORMATO 24H): ")

xadrez(int(A), int(B))
