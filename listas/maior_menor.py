numeros= []


for n in range(5):
        numero =int  (input("digite o numero "))
        numeros.append(numero)

maior = numeros[0]
menor = numeros[0]        


for numero in numeros:
    if numero > maior:
        maior =numero
    if numero <menor:
         menor = numero

print(f"Lista: {numeros}")
print(f"Maior número: {maior}")
print(f"Menor número: {menor}")