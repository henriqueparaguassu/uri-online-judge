n = int(input())
m = int(input())
soma = 0
if n < m:
    for i in range(n, m+1):
        if i % 13 != 0:
            soma += i
else:
    for i in range(m, n+1):
        if i % 13 != 0:
            soma += i
print(soma)
