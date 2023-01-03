# Escreva um algoritmo para ler o número total de eleitores de um município, o número de votos
# brancos, nulos e válidos. Calcular e escrever o percentual que cada um representa em relação ao total
# de eleitores.

def eleicao(eleitores, brancos, nulos):
    TOTAL = eleitores
    BRAN = (brancos * 100) / TOTAL
    NULO = (nulos * 100) / TOTAL
    VAL = ((TOTAL - BRAN - NULO) * 100) / TOTAL
    print("Numero de eleitores" + str(TOTAL), "\nNumero de votos em branco: " + str(BRAN)+"%", "\nNumero de votos nulos: " + str(NULO)+"%", "\nNumero de votos válidos: " + str(VAL)+"%")


E = input("Numero de eleitores: ")
B = input("Numero de votos em branco: ")
N = input("Numero de votos nulos: ")
eleicao(int(E), int(B), int(N))