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