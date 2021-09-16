inn, out, a = 0, 0, []
n = int(input())
for i in range(n):
    a.append(int(input()))
for i in range(n):
    if a[i] >= 10 and a[i] <= 20:
        inn += 1
    else:
        out += 1
print(inn, 'in')
print(out, 'out')
