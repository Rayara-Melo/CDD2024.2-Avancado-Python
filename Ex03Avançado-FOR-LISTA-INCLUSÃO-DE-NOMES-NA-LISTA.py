#CRIAR UM ARRAY TAMANHO 5 E PREENCHER COM OS NOMES DOS ALUNOS,
#INFORMADO PELO USUÁRIO

nomes = [" ", " ", " ", " ", " ", ]
tamanho = len(nomes)
for x in range(tamanho):
    nomes[x] = input("Digite os nomes dos alunos: ")
for i in range(tamanho):
    print(nomes[i])