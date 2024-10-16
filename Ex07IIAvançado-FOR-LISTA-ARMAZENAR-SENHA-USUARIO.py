#RESOLUÇÃO PROFESSOR#

# #FAÇA UM CÓDIGO PARA LER 5 NOMES DE USUÁRIOS E SUAS RESPECTIVAS SENHAS,
#E ARMAZENAR CADA LISTA EM UM ARRAY DIFERENTE, APÓS COMPLETAR A DIGITAÇÃO,
#IMPRIMIR, NOME SENHA E POSIÇÃO DOS DADOS NO ARRAY.

n = [" "]*5
senhas = [" "]*5
tam = len(n) #NÃO PRECISA TER DOIS "TAMANHOS", PORQUE SÃO DO MESMO TAMANHO

for i in range(tam):
    n[i] = input("Digite o nome: ")
    senhas[i] = input("Digite a senha: ")

for x in range(tam):
    print(f"Usuário {[x]}: Nome - {n[x]} e {senhas[x]}")