peso = float(input("Insira seu peso : "))

altura  = float(input("Insira sua altura : "))

imc = peso/(altura**2)

if imc<18.5:
    print(f"Seu IMC é: {imc:.2f}")
    print('Abaixo do Peso')
elif 18.5<= imc <24.9 :
    print(f"Seu IMC é: {imc:.2f}")
    print('Peso Normal')
elif 25<=imc <29.9:
    print(f"Seu IMC é: {imc:.2f}")
    print('SobrePeso')
else:
    print(f"Seu IMC é: {imc:.2f}")
    print('Obesidade')