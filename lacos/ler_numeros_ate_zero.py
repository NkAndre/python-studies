numero = int(input('Insira um numero (ou 0 para parar): '))

while numero != 0:
    ultimo_numero = numero
    print(f'numero digitado : {numero}')
    numero = int(input('Insira um numero (ou 0 para parar): '))

print(f'Aplicação finalizada com sucesso !\n ultimo numero digitado : {ultimo_numero}' )

