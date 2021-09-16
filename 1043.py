a, b, c = map(float, input().split())
if (c < a+b) and (c > abs(a-b)):
    print('Perimetro =', '%.1f' % (a+b+c))
else:
    print('Area =', '%.1f' % (((a+b)*c)/2))
