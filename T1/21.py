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
