number1 = int (input("Entre com o primeiro numero: "))

number2 = int (input("Entre com o segundo numero: "))

operacao  =  (input("1: +\n2: -\n3: *\n4: /\n Escolha: "))
if operacao =='1':
    resultado = number1 + number2
    print(f'O resultado da soma é: {resultado}')
elif operacao =='2':
    resultado = number1 - number2
    print(f'O resultado da Subtração é : {resultado}')
elif operacao == '3':
    resultado = number1 * number2
    print(f'O Resultado da Multiplicação é : {resultado}')
elif operacao == '4':
    if number2 !=0:
        resultado = number1 / number2
        print(f'O resultado da divisão é : {resultado}')
    else:
        print('Não é possivel dividir por zero')    
else:
    print('Numeros ou operador Invalidos!!')