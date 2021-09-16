v = int(input())
h = v//3600
v %= 3600
m = v//60
v %= 60
print('{}:{}:{}'.format(h, m, v))
