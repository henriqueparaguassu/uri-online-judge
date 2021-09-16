n, m = map(int, input().split())
if n > m:
    n -= m
    n = 24-n
    print('O JOGO DUROU {} HORA(S)'.format(n))
elif m > n:
    n = abs(n-m)
    print('O JOGO DUROU {} HORA(S)'.format(n))
elif m == n:
    print('O JOGO DUROU 24 HORA(S)')
