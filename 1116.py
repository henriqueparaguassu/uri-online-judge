n = int(input())
for i in range(n):
    a, b = map(float, input().split(" "))
    if b == 0:
        print("divisao impossivel")
    else:
        print("{}".format("%.1f" % (a/b)))
