# Analise os algoritmos abaixo e diga o que será impresso na tela ao serem executados:

def letras(numa, numb, numc):
    return (numa, numb, numc)


# a)
print("\n a)")

A, B, C = letras(10, 20, 0)
print("Escrever B: " + str(B))
B = 5
print("Escrever A, B: " + str(A), str(B))

# b)
print("\n b)")

A, B, C = letras(30, 20, 0)
C = A + B
print("Escrever C: " + str(C))
B = 10
print("Escrever B, C: " + str(B), str(C))
C = A + B
print("Escrever A, B, C: " + str(A), str(B), str(C))

# c)
print("\n letra c")

A, B, C = letras(10, 20, 0)
C = A
B = C
A = B
print("Escrever A, B, C: " + str(A), str(B), str(C))

# d)
print("\n d)")

A = 10
B = A + 1
A = B + 1
B = A + 1
print("Escrever A: " + str(A))
A = B + 1
print("Escrever A, B: " + str(A), str(B))

# e)
print("\n e)")

A, B, C = letras(10, 5, 0)
C = A + B
B = 20
A = 10
print("Escrever A, B, C: " + str(A), str(B), str(C))

# f)
print("\n f)")

X, Y, Z = letras(1, 2, 0)
Z = Y - X
print("Escrever Z: " + str(Z))
X = 5
Y = X + Z
print("Escrever X, Y, Z: " + str(X), str(Y), str(Z))
