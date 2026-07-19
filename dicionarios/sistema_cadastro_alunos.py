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
           print(f'Aluno {aluno["nome"]}  Cadastrado com sucesso!!')

                
            


    