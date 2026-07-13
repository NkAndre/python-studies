ladoA = int (input('Insira o primeiro lado: '))
ladoB = int (input('Insira o segundo lado: '))
ladoC = int (input('Insira o terceiro lado: '))


if ladoA <ladoB  + ladoC and ladoB < ladoA + ladoC and ladoC<ladoA+ladoB:
    print('Os lados formam um triângulo:')  
elif ladoA == ladoB == ladoC:
    print('Equilátero (três lados iguais)')
elif ladoA != ladoB and ladoB !=ladoC and ladoA != ladoC:
     print('Escaleno (três lados diferentes)')
else:
     print("Isósceles (dois lados iguais)")



   