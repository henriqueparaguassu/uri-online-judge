n1 = float(input())
n2 = float(input())
n3 = float(input())
n1, n2 = '%.1f' % n1, '%.1f' % n2
n1, n2, n3 = float(n1), float(n2), float(n3)
n1 = (n1*2+n2*3+n3*5)/10
print('MEDIA =', '%.1f' % n1)
