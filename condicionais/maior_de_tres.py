a = int (input('Digite o primeiro numero : '))
b = int (input('Digite o segundo numero : '))
c = int (input('Digite o terceiro numero : '))

if a > b and b>c:
    print(f'o primeiro numero {a} é maior que o segundo numero {b} e o segundo é maior que o terceiro numero {c}')

elif a>c and c>b:
    print(f'o primeiro numero {a} é maior que o terceiro numero,e terceiro numero {c}, maior que o segundo numero {b}')

elif b > a and a >c:
    print(f'o segundo numero {b} é maior que o primeiro numero {a}, e o primeiro numero {a} maior que o terceiro numero {c}')

elif b > c and c > a:
    print(f'o segundo numero {b} é maior que o terceiro numero {c}, e o terceiro numero {c} maior que o primeiro numero {a} ')

elif c> a and a > b:
    print(f'o terceiro numero {c} é maior que o primeiro numero {a}, e o primeiro numero {a}, é maior que o segundo numero {b}')

elif c > b and b > a :
    print(f'o terceiro numero {c} é maior que o segundo numero {b}, e o segundo numero {b} maior que o primeiro numero {a} ')

else:
    print('há numeros iguais : ')