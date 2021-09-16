n, m = 0, 1
while n != m:
    n, m = map(int, input().split())
    if n < m:
        print('Crescente')
    elif m < n:
        print('Decrescente')
