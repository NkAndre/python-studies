ano = int (input('Insira um ano e verifique se é bissexto ou não : '))

if ano % 400==0:
    print('ano bissexto')
elif ano % 100==0:
    print('Não é')
elif ano % 4==0:
    print('Bissexto')
else:
    print('Nao é Bissexto')