# Ler dois valores e imprimir uma das três mensagens a seguir:
# ‘Números iguais’, caso os números sejam iguais
# ‘Primeiro é maior’, caso o primeiro seja maior que o segundo;
# ‘Segundo maior’, caso o segundo seja maior que o primeiro.
def mensagem(num1, num2):
	if num1 > num2:
		print("Primeiro é maior")
	elif num2 > num1:
		print("Segundo é maior")
	else:
		print("Números iguais")

A = input("Primeiro número: ")
B = input("Segundo número: ")
mensagem(int(A), int(B))