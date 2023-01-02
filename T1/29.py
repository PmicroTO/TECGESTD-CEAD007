# 29) Ler 3 valores (considere que não serão informados valores iguais) e escrever a soma dos 2 maiores.

def dois_maiores(numbers):
    valor_ant = 0
    for x in numbers:
        for y in numbers:
            for z in numbers:
                if x > y and y > z:
                    print(x + y)


A = input("Primeiro número: ")
B = input("Segundo número: ")
C = input("Terceiro número: ")
dois_maiores([int(A), int(B), int(C)])
