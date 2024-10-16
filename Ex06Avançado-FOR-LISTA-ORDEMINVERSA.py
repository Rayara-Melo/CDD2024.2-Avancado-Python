#FAÇA UM CÓDIGO PARA LER 5 NÚMEROS E ARMAZENAR EM UM VETOR.
#APÓS A LEITURA TOTAL DOS 5 NÚMEROS,
#O CÓDIGO DEVE ESCREVER ESSES 5 NÚMEROS LIDOS NA ORDEM INVERSA.

A = [" ", " ", " ", " ", " ",]
tam = len(A)

for i in range(tam):
    A[i] = int(input("Digite um número: "))
for x in range(tam-1,0-1,-1):
        print(A[x])