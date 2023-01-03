# Para A = V, B = V e C = F, qual o resultado da avaliação das seguintes expressões:
# a) (A e B) ou (A xou B)
# b) (A ou B) e (A e C)
# c) A ou C e B xou A e não B
A = True
B = True
C = False

a = (A and B) or (A ^ B)
b = (A or B) and (A and C)
c = A or C and B ^ A and not B

print(a, b, c)
