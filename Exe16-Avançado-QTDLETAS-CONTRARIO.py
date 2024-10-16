#FAÇA UMA FUNÇÃO QUE RECEBA UM TEXTO COMO ARGUMENTO, MOSTRE A QUANTIDADE
#DE LETRAS E TAMBÉM IMPRIMA O TEXTO AO CONTRÁRIO.

soma = 0
texto = [" "]
tam = len(texto)

texto = input("Insira o texto: ")
for x in texto:
    if x in "abcdefghijlmnopqrstuvxzwkyABCDEFGHIJLMNOPQRSTUWYK":
        soma += 1
    print(texto)
print(f"O texto informado contém {soma} LETRAS")