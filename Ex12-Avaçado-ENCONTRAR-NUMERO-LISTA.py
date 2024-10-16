#RESOLUÇÃO DO PROFESSOR

numeros = [0]*10
tam = len(numeros)
cont = 0

for x in range(tam):
    numeros[x] = int(input("Digite um número: "))
x = int(input("Informe um número que deseja procurar: "))

for z in range(tam):
    if x == numeros[z]:
        cont+=1
print(cont)


