def estoque(atual, max, min):
    ME = (max + min) / 2
    print("Quantidade média: " + str(ME))
    if atual >= ME:
        print("Não efetuar compra")
    else:
        print("Efetuar compra")


A = input("Quantidade atual: ")
B = input("Quantidade máxima: ")
C = input("Quantidade mínima: ")
estoque(int(A), int(B), int(C))
