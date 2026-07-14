
numero = int(input('Insira um numero (ou 0 para sair): '))
maior_numero = numero
while numero != 0:
    if numero>maior_numero:
        maior_numero = numero
   
    numero = int(input("Insira um número (ou 0 para sair): "))

print(f"O maior numero foi: {maior_numero}")


