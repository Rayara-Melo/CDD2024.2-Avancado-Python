#FAÇA UM ALGORITMO QUE LEIA 10 VALORES DO TIPO INTEIRO E ARMAZENE-OS EM UM VALOR.
#A SEGUIR, O ALGORITMO  DEVERÁ INFORMAR.
#1 - TODOS OS NÚMEROS PARES QUE EXISTEM NO VETOR;
#2 - O MENOR E O MAIOR VALORS EXISTENTE NO VETOR;
#3 - QUANTOS DOS VALORES DO VETOR SÃO MAIORES QUE A MÉDIA DESSES VALORES.


lista = [""]*3
tam = len(lista)
maior = 0
menor = 100000000000000000000

for i in range(tam):
    lista[i] = int(input("Digite um número: "))

for x in range(tam):
    if lista[x] % 2 == 0:
        print(lista[x], end=" ")
maior = max(lista)
menor = min(lista)

