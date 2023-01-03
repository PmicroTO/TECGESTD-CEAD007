# Ler 2 valores, calcular e escrever a soma dos inteiros existentes entre os 2 valores lidos (incluindo
# os valores lidos na soma). Considere que o segundo valor lido poderá ser maior ou
# menor que o primeiro valor lido, ou seja, deve-se testá-los.

A = input("Primeiro número: ")
B = input("Segundo número: ")

a = int(A)
b = int(B) + 1

soma = 0

if A < B:
    for x in range(a, b):
        soma += x
else:
    print("Primeiro número maior que o segundo")

print(soma)
