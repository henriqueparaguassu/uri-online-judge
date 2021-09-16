a = int(input())
b = int(input())
if b > a:
    for i in range(a, b):
        if (i % 5 == 2) or (i % 5 == 3):
            print(i)
elif a > b:
    j = []
    for i in range(a, b, -1):
        if (i % 5 == 2) or (i % 5 == 3):
            j.append(i)
    j.sort()
    for i in j:
        print(i)
