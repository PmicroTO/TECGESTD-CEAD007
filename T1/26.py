# Faça um algoritmo para ler: quantidade atual em estoque, quantidade máxima em estoque e
# quantidade mínima em estoque de um produto. Calcular e escrever a quantidade média ((quantidade
# média = quantidade máxima + quantidade mínima)/2). Se a quantidade em estoque for maior ou igual
# a quantidade média escrever a mensagem 'Não efetuar compra', senão escrever a mensagem 'Efetuar
# compra'.
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
