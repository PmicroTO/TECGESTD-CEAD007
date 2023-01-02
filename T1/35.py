LA = 2.90
LG = 3.30

c = input("[A] álcool ou [G] gasolina?")

if c == "A":
    a = input("Litros de álcool: ")
    A = float(a)
    if A > 20:
        print(A * (LA * 0.95))
    else:
        print(A * (LA * 0.97))
elif c == "G":
    g = input("Litros de gasolina: ")
    G = float(g)
    if G > 20:
        print(G * (LG * 0.94))
    else:
        print(G * (LG * 0.96))
else:
    print("Opções válidas: G ou A")
