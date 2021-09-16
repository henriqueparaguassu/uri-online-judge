lista = [int(x) for x in input().split()]
valor = lista[:]
lista.sort()
for i in range(len(lista)):
    print(lista[i])
print()
for i in range(len(valor)):
    print(valor[i])
