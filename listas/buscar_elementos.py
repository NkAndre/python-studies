linguagens = ["Python", "Java", "PHP", "JavaScript", "C#"]

print(f'Lista atual: {linguagens}')

linguagens_minusculas = [l.lower() for l in linguagens]
buscar = input("Qual Linguagem  Deseja Procurar ?").lower()
if buscar in linguagens_minusculas:
    posicao = linguagens_minusculas.index(buscar)

    print(f'Linguagem encontrada : {linguagens [posicao]} , está na posição {posicao}.!')
else:
    print('Nao encontrada')