import os 
os.system('cls')

cadastro_lista = []

while True:
    selecionar = int(input("Selecione uma Opção: \n1 = Cadastrar \n2 = Ver cadastros\n3 = Sair\n"))
    if selecionar == 1:
        nome = input("Informe nome: ")
        idade = int(input("Qual sua idade: "))
        cpf = input("Informe CPF:") 
        cpf_mascarado = "{}.{}.{}-{}".format(cpf[:3], cpf[3:6], cpf[6:9], cpf[9:])

        # Verificar se o CPF já está cadastrado
        cpf_cadastrado = False
        for item in cadastro_lista:
            if item[2] == cpf_mascarado:
                cpf_cadastrado = True
                break

        if cpf_cadastrado:
            print("CPF já está cadastrado. Tente novamente.")
        else:
            cadastro_lista.append([nome, idade, cpf_mascarado])
            print("Cadastro realizado com sucesso.")

    elif selecionar == 2:
      
        for item in cadastro_lista:
            print("Nome: {}\nIdade: {}\nCPF: {}\n".format(item[0], item[1], item[2]))
    elif selecionar == 3:
        break
    else:
        print("Opção inválida. Tente novamente.")
