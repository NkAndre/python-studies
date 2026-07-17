   #Projeto : Mini Listas de Compras 
menu = ''
produtos = []  

while  menu!="5":
    
    menu = (input('1 - Adicionar Produto\n 2 - Remover Produto\n 3 - Buscar Produto\n 4 - Mostrar Lista\n 5 - Sair\n Escolha :  '))
    if menu == "1":
   
        while True:

            produto =  (input("Adicione produto  (ou digite sair para voltar  ):  "))
            if produto.lower() == 'sair':
                break
            produtos.append(produto)
            print(f'Produtos adicionados : {produtos}')


 
