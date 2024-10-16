#ESCREVA UM ALGORITMO QUE SOLICITE AO USUÁRIO A ENTREDA DE 5 NOMES,
# E QUE EXIBA A LISTA DESSES NOMES NA TELA.
#APÓS EXIBIR ESSA LISTA, O PROGRAMA DEVE MOSTRAR TAMBÉM OS NOMES NA ORDEM INVERSA
#EM QUE USUÁRIO OS DIGITOU, UM POR LINHA.

lista = [""]*3
tam = len(lista)

for i in range(tam):
    lista[i] = int(input("Digite um número: "))

print(lista)
lista.reverse()
print(lista)


