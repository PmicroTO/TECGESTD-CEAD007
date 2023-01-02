val_x = [3, 150, 7, -2, 50]
val_y = [2, 3, -1, 5, 3]

for X in val_x:
    for Y in val_y:
        Z = (X * Y) + 5
        if Z <= 0:
            resposta = "A"
        elif Z <= 100:
            resposta = "B"
        else:
            resposta = "C"
        print(" Valor de X: " + str(X) + ", Valor de Y: " + str(Y) +
              ", Valor de Z: " + str(Z) + ", Resposta: " + resposta)
