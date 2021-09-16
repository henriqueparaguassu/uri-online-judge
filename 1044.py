n = input()
A = n.split()
x = int(A[0])
y = int(A[1])
if (x % y == 0) or (y % x == 0):
    print('Sao Multiplos')
else:
    print('Nao sao Multiplos')
