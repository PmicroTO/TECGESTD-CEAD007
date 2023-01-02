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
