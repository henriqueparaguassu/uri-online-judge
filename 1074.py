n = int(input())
for i in range(n):
    a = int(input())
    if a % 2 == 0 and a > 0:
        print('EVEN POSITIVE')
    elif a % 2 == 0 and a < 0:
        print('EVEN NEGATIVE')
    elif a % 2 != 0 and a > 0:
        print('ODD POSITIVE')
    elif a % 2 != 0 and a < 0:
        print('ODD NEGATIVE')
    elif a == 0:
        print("NULL")
