numeros= []
for n in range(5):
        numero =int  (input("digite o numero "))
        numeros.append(numero)
print(f'Lista Original :{numeros}')
ordenada = numeros.copy()
ordenada.sort()

reversa = numeros.copy()

reversa.sort(reverse=True)
print(f'Lista ordenada: {ordenada}')
print(f'Decrescente :  {reversa}')