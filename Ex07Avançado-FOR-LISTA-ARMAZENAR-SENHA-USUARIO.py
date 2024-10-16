#FAÇA UM CÓDIGO PARA LER 5 NOMES DE USUÁRIOS E SUAS RESPECTIVAS SENHAS,
#E ARMAZENAR CADA LISTA EM UM ARRAY DIFERENTE, APÓS COMPLETAR A DIGITAÇÃO,
#IMPRIMIR, NOME SENHA E POSIÇÃO DOS DADOS NO ARRAY.

n = [" ", " ", " ", " ", " ",]
senhas = [" ", " ", " ", " ", " ",]
tam = len(n)

for i in range(tam):
    n[i] = input("Digite o nome: ")
    senhas[i] = input("Digite a senha: ")
for x in range(tam):
    print(f"Usuário {x}: {n[x]}, {senhas[x]}")