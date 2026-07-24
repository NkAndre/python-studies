def calcular():
    numero = int (input('Digite um numero: '))
    for n in  range(0,11):
        resultado = numero * n
        print(f'{numero} X {n} = {resultado}')
calcular()
