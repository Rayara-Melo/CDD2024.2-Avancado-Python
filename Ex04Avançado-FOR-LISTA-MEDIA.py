#ESCREVA UM CÓDIGO QUE PERMITA A LEITURA DAS NOTAS DE UMA TURMA DE 5 ALUNOS E GUARDE
#NUM VETOR. CALCULAR A MÉDIA DA TURMA E CONTAR QUANTOS OBTIVERAM NOTA ACIMA DESTA MÉDIA CALCULADA
#ESCREVER A MÉDIA DA TURMA E O RESULTADO DA CONTAGEM.

notas = [" ", " ", " ", " ", " ", ]
tamanho = len(notas)
soma = 0
cont = 0
for x in range(tamanho):
    notas[x] = float(input("Digite a nota: "))

for i in range(tamanho):
    soma = soma + notas[i]
media = soma / tamanho

for y in range(tamanho):
    if notas[y] > media:
        cont+=1
print(f"Temos {cont} alunos com nota maior que a media: {media}")

