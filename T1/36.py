# Escreva um algoritmo que leia as idades de 2 homens e de 2 mulheres (considere que as idades
# dos homens serão sempre diferentes entre si, bem como as das mulheres). Calcule e escreva a soma
# das idades do homem mais velho com a mulher mais nova, e o produto das idades do homem mais
# novo com a mulher mais velha.
def idades(h1, h2, m1, m2):
    if h1 > h2:
        hv = h1
        hj = h2
    else:
        hv = h2
        hj = h1
    if m1 > m2:
        mv = m1
        mj = m2
    else:
        mv = m2
        mj = m1
    soma = hv + mj
    produto = hj * mv
    print("Soma da idade do homem mais velho com a da mulher mais nova: " + str(soma),
    " Produto das idades do homem mais novo com a mulher mais velha: " + str(produto))


H1 = input("Idade do primeiro homem: ")
H2 = input("Idade do segundo homem: ")
M1 = input("Idade da primeira mulher: ")
M2 = input("Idade da segunda mulher: ")
idades(int(H1), int(H2), int(M1), int(M2))