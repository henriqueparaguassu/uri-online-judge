cont, media = 0.0, 0.0
for i in range(6):
    valor = float(input())
    if valor > 0:
        cont += 1
        media += valor
print(round(cont), 'valores positivos')
print('%.1f' % (media/cont))
