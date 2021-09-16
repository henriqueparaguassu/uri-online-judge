impar, par, neg, pos, a = 0, 0, 0, 0, []
for i in range(5):
    a.append(int(input()))
for i in range(5):
    if a[i] > 0:
        pos += 1
    if a[i] < 0:
        neg += 1
    if a[i] % 2 == 0:
        par += 1
    if a[i] % 2 != 0:
        impar += 1
print(par, 'valor(es) par(es)')
print(impar, 'valor(es) impar(es)')
print(pos, 'valor(es) positivo(s)')
print(neg, 'valor(es) negativo(s)')
