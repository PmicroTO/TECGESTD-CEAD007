def qual_maior(num1, num2):
    if num2 > num1:
        print("O maior valor é: " + str(num2))
    else:
        print("O maior valor é: " + str(num1))


A = input("Primeiro valor: ")
B = input("Segundo valor: ")
qual_maior(int(A), int(B))
