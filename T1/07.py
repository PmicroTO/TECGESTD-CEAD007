def idade_dias(anos, meses, dias):
    anos_d = anos * 365
    meses_d = meses * 30
    dias_d = dias
    print(anos_d + meses_d + dias_d)


ANOS = input("Quantos anos: ")
MESES = input("Quantos meses: ")
DIAS = input("Quantos dias: ")

idade_dias(int(ANOS), int(MESES), int(DIAS))
