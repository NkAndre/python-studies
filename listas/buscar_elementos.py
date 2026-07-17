linguagens = ["Python", "Java", "PHP", "JavaScript", "C#"]

print(f'Lista atual: {linguagens}')


buscar = (input("Qual Linguagem  Deseja Procurar ?"))
if buscar in linguagens:
    posicao = linguagens.index(buscar)

    print(f'Linguagem encontrada : {buscar} , está na posição {posicao}.!')
else:
    print('Nao encontrada')