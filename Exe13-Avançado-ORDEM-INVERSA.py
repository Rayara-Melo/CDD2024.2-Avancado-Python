#ESCREVA UM ALGORITMO QUE SOLICITE AO USUÁRIO A ENTREDA DE 5 NOMES,
# E QUE EXIBA A LISTA DESSES NOMES NA TELA.
#APÓS EXIBIR ESSA LISTA, O PROGRAMA DEVE MOSTRAR TAMBÉM OS NOMES NA ORDEM INVERSA
#EM QUE USUÁRIO OS DIGITOU, UM POR LINHA.


lista = [""]*3
tam = len(lista)

for i in range(tam):
    lista[i] = input("Digite um número: ")
print(lista)

for x in range(tam-1,-1,-1):
    print(lista[x], end=" ")



