A = 10
B = 20

print("Originalmente temos ", "A=" + str(A), "B=" + str(B))

tmp_A = B
tmp_B = A

A = tmp_A
B = tmp_B

print("Invertendo valores de A e B temos ", "A=" + str(A), "B=" + str(B))