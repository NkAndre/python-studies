linguagens = ['Java', 'Python', 'PHP', 'JavaScript']

print(f'Lista atual: {linguagens}')

remover = input("Qual linguagem deseja remover? ")
if remover in linguagens:
    linguagens.remove(remover)
else:
    print('Invalido, nao existe essa linguagem na lista!')


print(f'Lista atualizada: {linguagens}')