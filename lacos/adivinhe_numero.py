import random


numero_sorteado = random.randint(1, 10)

numero = int(input("Insira um numero"))


while numero != numero_sorteado:
    print(f'Errado!\nseu numero {numero} \nNumero da máquina: {numero_sorteado}')
    numero = int(input("Tente novamente: "))

print(f"Parabéns! Você acertou!\nSeu número: {numero}\nNúmero da máquina: {numero_sorteado}")
