#FAÇA UMA FUNÇÃO QUE CONTE QUANTAS VOGAIS TEM UM TEXTO.
# #TEXTO: O rato roeu a roupa do Rei de Roma

soma = 0
n = input("Insira o texto: ")
for x in n:
    if x in "aeiouAEIOU":
     soma += 1
print(f"O texto informado contém {soma} vogais")
