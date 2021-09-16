x = []
for i in range(100):
    x.append(int(input()))
for i in range(100):
    if x[i] == max(x):
        cont = i+1
print(max(x))
print(cont)
