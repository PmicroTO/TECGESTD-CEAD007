# Uma loja está levantando o valor total de todas as mercadorias em estoque. Escreva um algoritmo
# que permita a entrada das seguintes informações: a) o número total de mercadorias no estoque; b) o
# valor de cada mercadoria. Ao final imprimir o valor total em estoque e a média de valor das
# mercadorias.

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
