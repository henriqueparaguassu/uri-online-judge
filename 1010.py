a, b, c = map(float, input().split())
d, e, f = map(float, input().split())
int(a)
int(b)
int(d)
int(e)
c, f = '%.2f' % c, '%.2f' % f
c, f = float(c), float(f)
print('VALOR A PAGAR: R$', '%.2f' % (b*c+e*f))
