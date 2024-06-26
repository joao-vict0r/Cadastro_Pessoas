import os 
os.system('cls')
cadastro_lista = []

while True:
    selecionar = int(input("Selecione uma Opção: \n1 = Cadastrar \n2 = Ver cadastros \n3 = Achar cadastro \n4 = Excluir Cadastro \n5 = Sair\n"))
    if selecionar == 1:
        nome = input("Informe nome: ")
        data_nascimento = input("Informe a data de nascimento somente os numeros (DD/MM/AAAA): ")
        cpf = input("Informe CPF:") 
        cpf_mascarado = "{}.{}.{}-{}".format(cpf[:3], cpf[3:6], cpf[6:9], cpf[9:])
        data_nascimento_formatada = "{}/{}/{}".format(data_nascimento[:2], data_nascimento[2:4], data_nascimento[4:])
        # Verificar se o CPF já está cadastrado
        cpf_cadastrado = False
        for item in cadastro_lista:
            if item[2] == cpf_mascarado:
                cpf_cadastrado = True
                break
        if cpf_cadastrado:
            print("CPF já está cadastrado. Tente novamente.")
        else:
            cadastro_lista.append([nome, data_nascimento_formatada, cpf_mascarado])
            print("Cadastro realizado com sucesso.")
    
    elif selecionar == 2:
        for item in cadastro_lista:
            print("Nome: {}\nIdade: {}\nCPF: {}\n".format(item[0], item[1], item[2]))
    
    #Procura de Cadastro pelo CPF 
    elif selecionar == 3:
        cpf_busca = input("Insira o CPF para encontrar o cadastro correspondente: ")
        cpf_busca_mascarado = "{}.{}.{}-{}".format(cpf_busca[:3], cpf_busca[3:6], cpf_busca[6:9], cpf_busca[9:])
        cpf_encontrado = False
    #condição que encontra cadastro na lista
        for item in cadastro_lista:
         if item[2] == cpf_busca_mascarado:
            cpf_encontrado = True
            print("Nome: {}\nIdade: {}\nCPF: {}\n".format(item[0], item[1], item[2]))
        if not cpf_encontrado:
            print("Não foi encontrado cadastro com este CPF: {}".format(cpf_busca_mascarado))
        
    elif selecionar == 4:
        cpf_busca = input("Insira o CPF para exclusão do cadastro: ")
        cpf_busca_mascarado = "{}.{}.{}-{}".format(cpf_busca[:3], cpf_busca[3:6], cpf_busca[6:9], cpf_busca[9:])
        cpf_encontrado = False

        for item in cadastro_lista:
            if item[2] == cpf_busca_mascarado:
                cpf_encontrado = True
                cadastro_lista.remove(item)  # Remover o item correspondente
                print("Cadastro excluído")
                break  # Sair do loop depois que o cadastro for excluído

            if not cpf_encontrado:
             print("Não foi encontrado cadastro com este CPF: {}".format(cpf_busca_mascarado))


            
    elif selecionar == 5:
        break
    else:
        print("Opção inválida. Tente novamente.")
