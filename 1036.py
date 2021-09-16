a, b, c = map(float, input().split())
delta = (b**2)-(4*a*c)
d = 2*a
if (delta < 0) or (d == 0):
    print('Impossivel calcular')
else:
    x1 = ((0-b)+delta**(1/2))/(2*a)
    x2 = ((0-b)-delta**(1/2))/(2*a)
    print('R1 =', '%.5f' % x1)
    print('R2 =', '%.5f' % x2)
