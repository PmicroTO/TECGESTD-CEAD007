nome = input("Nome do produto: ")
quant = input("Quantidade: ")
preco = input("Preço unitário: ")

TO = float(quant) * float(preco)
Q = int(quant)
N = nome
if Q <= 5:
    DE = 2/100
    DES = "2%"
elif Q > 5 and Q <= 10:
    DE = 3/100
    DES = "3%"
elif Q > 10:
    DE = 5/100
    DES = "5%"

    TD = TO - (TO * DE)
    print("Produto: " + N, "Quantidade: " + str(Q), "Valor Total: " +
          str(TO), "Desconto: " + str(DES), "Total  pagar: " + str(TD))
