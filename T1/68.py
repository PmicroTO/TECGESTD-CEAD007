MER = input("Número de mercadorias em estoque: ")

me = int(MER) + 1
TO = 0

for x in range(1, me):
    VAL = input("Valor da mercadoria: ")
    va = float(VAL)
    TO += va

MEDIA = TO / me

print("Valor total em estoque: " + str(TO),
      ", Valor médio das mercadorias: " + str(MEDIA))
