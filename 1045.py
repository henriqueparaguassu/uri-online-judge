lista = [float(x) for x in input().split()]
lista.sort()
c, b, a = lista[0], lista[1], lista[2]
if a >= b+c:
    print('NAO FORMA TRIANGULO')
else:
    if (a**2 == b**2+c**2):
        print('TRIANGULO RETANGULO')
    if (a**2 > b**2+c**2):
        print('TRIANGULO OBTUSANGULO')
    if (a**2 < b**2+c**2):
        print('TRIANGULO ACUTANGULO')
    if (a == b == c):
        print('TRIANGULO EQUILATERO')
    if (a == b != c) or (a == c != b) or (b == c != a):
        print('TRIANGULO ISOSCELES')
