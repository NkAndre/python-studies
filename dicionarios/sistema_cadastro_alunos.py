menu = ''

alunos = []
while  menu!="5":
    print("\n===== CADASTRO DE ALUNOS =====")
    menu = (input('1 - Cadastrar Alunos\n 2 - Listar Alunos\n 3 - Buscar aluno\n 4 -  Remover aluno\n 5 - Sair\n Escolha :  '))

    if menu =='1':
        while True:
           
           

           if alunos.lower() == 'sair':
                break
                alunos["nome"] = input("Digite o nome: ")
                alunos["idade"] = int(input("Digite a idade: "))
                alunos["cidade"] = input("Digite a cidade: ")
                


    