#PREENCHER UM VETOR (A) COM 10 NÚMEROS. # LOGO EM SEGUIDA,
#LER MAIS UM NÚMERO E GUARDAR EM UMA VARIAVEL. ARMAZENAR EM UM VETOR M O RESULTADO
#DE CADA ELEMENTO DE A MULTIPLICADO PELO VALOR X NO FINAL IMPRIMIR O VETOR M.

A = [" ", " ", " ",]
x = 0
M = [" ", " ", " ",]
tam = len(A)
for i in range(tam):
    A[i] = int(input("Digite um número: "))
x = int(input("Digite o multiplicador: "))
for x in range(tam):
    M[x] = A[x]*x
print(A)
print(x)
print(M)
