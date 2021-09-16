n = int(input())
mes = ['', 'January', 'February', 'March', 'April', 'May', 'June',
       'July', 'August', 'September', 'October', 'November', 'December']
for i in range(1, 13):
    if n == i:
        print(mes[i])
