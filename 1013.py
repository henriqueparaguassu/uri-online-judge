valor = input().split()
maior = -999999999999999
for i in range(3):
    if int(valor[i]) > maior:
        maior = int(valor[i])
print(maior, 'eh o maior')
