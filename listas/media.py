notas = []
total = 0
for n in range(5):
        nota =int  (input("digite a nota : "))
        notas.append(nota)
        total+=nota
        media = total/len(notas)
print(notas)
print(media)
        