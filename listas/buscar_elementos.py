linguagens = ["Python", "Java", "PHP", "JavaScript", "C#"]

print(f'Lista atual: {linguagens}')


buscar = (input("Qual Linguagem  Deseja Procurar ?"))
if buscar in linguagens:
    print('Linguagem encontrada!')
else:
    print('Nao encontrada')