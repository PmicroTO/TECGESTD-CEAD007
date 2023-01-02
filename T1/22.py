def salario(horas_mes, valor_hora):
    H_EXTRA_TEMPO = horas_mes - 160
    H_EXTRA_VALOR = valor_hora * 1.5
    if H_EXTRA_TEMPO > 0:
        SAL = (valor_hora * horas_mes) + (H_EXTRA_TEMPO * H_EXTRA_VALOR)
    else:
        SAL = valor_hora * horas_mes

    print("Horas totais trabalhadas: " + str(horas_mes) + ", sendo " + str(H_EXTRA_TEMPO) + " de horas extras" + ", salário do mês: " + str(SAL))


A = input("Horas trabalhadas mensais: ")
B = input("Valor da hora: ")
salario(int(A), float(B))