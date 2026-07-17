   #Projeto : Mini Listas de Compras 
menu = ''
produtos = []  

while  menu!="5":
    print("\n===== MINI LISTA DE COMPRAS =====")
    menu = (input('1 - Adicionar Produto\n 2 - Remover Produto\n 3 - Buscar Produto\n 4 - Mostrar Lista\n 5 - Sair\n Escolha :  '))
    if menu == "1":
   
        while True:

            produto =  (input("Adicione produto  (ou digite sair para voltar  ):  "))
            if produto.lower() == 'sair':
                break
            produtos.append(produto)
            print(f'Produtos adicionados : {produtos}')
    elif menu == '2':
     if len(produtos) == 0:
            print('A lista está Vazia')
     else:
        print(f'Lista atual : {produtos}')
        remover = input("Qual Produto deseja remover? ")
       
        if remover in produtos:
                produtos.remove(remover)
                print(f'Produto removido com sucesso! Lista Atual {produtos}')
        else:
             print('Produto indisponivel ou nao encontrado')
    elif menu == "3":
        produtos_minusculos = [l.lower() for l in produtos]
        buscar = input("Qual produto deseja procurar? ").lower()

        if buscar in produtos_minusculos:
            posicao = produtos_minusculos.index(buscar)
            print(f"Produto encontrado: {produtos[posicao]}.")
        else:
            print("Produto não encontrado.")
    elif menu == '4':
          if len(produtos) == 0:
           print("A lista está vazia.")
          else:
           print("\n===== LISTA DE COMPRAS =====")
           for produto in produtos:
               print(f"- {produto}")
    elif menu == "5":
        print('Programa encerrado !')






 
