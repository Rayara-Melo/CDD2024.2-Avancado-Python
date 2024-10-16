#FAÇA UM PROGRAMA PARA IMPRIMIR:
#1
#2 2
#3 3 3

n = int(input("Digite o número: "))
for x in range(1,n+1):
        for i in range(x):
            print(x, end = "  ")
        print()

