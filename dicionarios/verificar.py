aluno = {
    'nome': 'André',
    'idade': 17,
    'curso': 'inglês'
}

buscar = input("Qual informação deseja procurar? ")

if buscar in aluno:
    print(f"Valor: {aluno[buscar]}")
else:
    print("Não existe.")