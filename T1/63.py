# Escreva um algoritmo para ler 10 números e ao final da leitura escrever a soma total dos 10
# números lidos.
soma = 0
for x in range(10):
    A = input("Digite um número: ")
    a = int(A)
    soma += a
print(soma)
