# Faça um algoritmo que leia a idade de uma pessoa expressa em anos, meses e dias e escreva a idade
# dessa pessoa expressa apenas em dias. Considerar ano com 365 dias e mês com 30 dias.

def idade_dias(anos, meses, dias):
    anos_d = anos * 365
    meses_d = meses * 30
    dias_d = dias
    print(anos_d + meses_d + dias_d)


ANOS = input("Quantos anos: ")
MESES = input("Quantos meses: ")
DIAS = input("Quantos dias: ")

idade_dias(int(ANOS), int(MESES), int(DIAS))
