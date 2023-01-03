# Um posto está vendendo combustíveis com a seguinte tabela de descontos:
# até 20 litros, desconto de 3% por litro
# acima de 20 litros, desconto de 5% por litro
# até 20 litros, desconto de 4% por litro
# acima de 20 litros, desconto de 6% por litro
# Álcool
# Gasolina
# Escreva um algoritmo que leia o número de litros vendidos e o tipo de combustível (codificado da
# seguinte forma: A-álcool, G-gasolina), calcule e imprima o valor a ser pago pelo cliente sabendo-se
# que o preço do litro da gasolina é R$ 3,30 e o preço do litro do álcool é R$ 2,90.
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
