menu = ''
alunos = []

while  menu!="5":
    print("\n===== CADASTRO DE ALUNOS =====")
    menu = (input('1 - Cadastrar Alunos\n 2 - Listar Alunos\n 3 - Buscar aluno\n 4 -  Remover aluno\n 5 - Sair\n Escolha :  '))

    if menu =='1':
        while True:
           
       
           opcao =  (input("Cadastre Aluno  (ou digite 'sair' para voltar  ):  "))
           if opcao.lower() == 'sair':
                break
           aluno = {}
           aluno["nome"] = input("Digite o nome: ")
           aluno["idade"] = int(input("Digite a idade: "))
           aluno["cidade"] = input("Digite a cidade: ")
           alunos.append(aluno)     
           print(f'Aluno {aluno["nome"]} Cadastrado com sucesso!!')

    if menu =='2':
        if len(alunos) ==0:
            print('A lista está vazia')
        else:
            for aluno in alunos:

             for chave, valor in aluno.items():
                print(f'{chave} : {valor}')
                print('-' * 20)
    
    if menu =='3':
        if len(alunos) ==0:
            print('a lista está vazia, não será possivel realizar a busca.')
        else:
            buscar = input('Digite o nome do aluno :')
            encontrado = False
            for aluno in alunos:
                if aluno['nome'] ==buscar:
                     print(f'Aluno {aluno["nome"]} encontrado!!')
                     print(f'Nome: {aluno["nome"]}')
                     print(f'Idade: {aluno["idade"]}')
                     print(f'Cidade: {aluno["cidade"]}')

                     encontrado = True
                     break
            if not encontrado:
                print("Aluno não encontrado.")

    if menu =='4':
         if len(alunos) ==0:
            print('a lista está vazia, não será possivel realizar a busca.')
         else:
             buscar = input('Digite o nome do aluno :')
             encontrado = False
             for aluno in alunos :
                 if aluno['nome'] ==buscar:
                     alunos.remove(aluno)
                     encontrado = True
                     print("Aluno removido com sucesso!")
                     break
             if not encontrado:
                 print('nao encontrado')
    elif menu == "5":
        print('Programa encerrado !')
    else:
        print("Opção inválida!")
             


                    
    


                
            


    