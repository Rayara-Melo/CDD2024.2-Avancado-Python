#ALTERE O SISTEMA ANTERIOR E FAÇA UM SISTEMA  DE LOGIN, PEDINDO A SENHA
#DO USUÁRIO E MOSTRANDO SEU NOME E A MENSAGEM, LOGIN EFETUADO COM SUCESSO.

#EXERCICIO ANTERIOR:  #FAÇA UM CÓDIGO PARA LER 5 NOMES DE USUÁRIOS E
# SUAS RESPECTIVAS SENHAS,E ARMAZENAR CADA LISTA EM UM ARRAY DIFERENTE,
#APÓS COMPLETAR A DIGITAÇÃO, IMPRIMIR, NOME SENHA E POSIÇÃO DOS DADOS NO ARRAY.

tam = 5
nomes = [""]*tam
senhas = [""]*tam
opcao = 0
tentativas = 3
login = False
while opcao != 4 :
    print("Digite uma opção desejada: \n 1 - CADASTRO\n 2 - LOGIN\n 3 - MOSTRAR USUÁRIOS\n 4 - SAIR")
    opcao = input("Digite sua opção: ")

    match opcao:
        case "1":
            for i in range(tam):
                user_existe = True
                while user_existe == True:
                    nome_tent = input(f'Cadastro do usuário {i+1}: ')
                    if nome_tent not in nomes:
                        nomes[i] = nome_tent
                        user_existe = False
                    else:
                        print("Usuário já existe!")
                senhas[i] = input(f"Cadastro da senha {i+1}: ")
            print("Todos os usuários cadastros")
        case "2":
            while tentativas > 0 and login == False:
                nome_tentativa = input("Digite o usuário: ")
                if nome_tentativa not in nomes:
                    print("Usuário não cadastrado")
                    break
                senha_tentativa = input("Digite sua senha: ")
                for x in range(tam):
                    if nomes[x] == nome_tentativa and senha_tentativa == senhas[x]:
                        print("Login concluído com sucesso")
                        login = True
                if login == False:
                    tentativas-=1
                    print(f"Usuário ou senha incorreta, tente novamente. Voçê tem {tentativas} tentativas!")
                    if tentativas == 0:
                        print("Tentativas esgotadas!")
            tentativas = 3
            login = False
        case "3":
            print("Todos os usuários cadastros são:")
            for i in range(tam):
                print(f"Posição {i}: {nomes[i]}, {senhas[i]}")
        case "4":
            print("Menu encerrado!!!")
            break

