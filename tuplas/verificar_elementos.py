linguagens = ("Python", "Java", "PHP", "JavaScript", "C#")
print(linguagens)

linguagens_minusculas = [l.lower() for l in linguagens]
buscar = input("Qual Linguagem  Deseja Procurar ?").lower()
if buscar in linguagens_minusculas:
    posicao = linguagens_minusculas.index(buscar)
    print('Linguagem encontrada!')
else:
    print('Nao encontrada')
