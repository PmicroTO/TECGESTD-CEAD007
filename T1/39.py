A = True
B = True
C = False

a = (A and B) or (A ^ B)
b = (A or B) and (A and C)
c = A or C and B ^ A and not B

print(a, b, c)
