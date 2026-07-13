ladoA = int(input("Insira o primeiro lado: "))
ladoB = int(input("Insira o segundo lado: "))
ladoC = int(input("Insira o terceiro lado: "))

if ladoA < ladoB + ladoC and ladoB < ladoA + ladoC and ladoC < ladoA + ladoB:

    print("Os lados formam um triângulo.")

    if ladoA == ladoB == ladoC:
        print("Equilátero (três lados iguais)")

    elif ladoA == ladoB or ladoA == ladoC or ladoB == ladoC:
        print("Isósceles (dois lados iguais)")

    else:
        print("Escaleno (três lados diferentes)")

else:
    print("Os valores não formam um triângulo.")