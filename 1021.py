valor = float(input())
n100 = 0
n50 = 0
n20 = 0
n10 = 0
n5 = 0
n2 = 0
m1, m50, m25, m10, m5 = 0, 0, 0, 0, 0
n100 = valor//100
valor %= 100
n50 = valor//50
valor %= 50
n20 = valor//20
valor %= 20
n10 = valor//10
valor %= 10
n5 = valor//5
valor %= 5
n2 = valor//2
valor %= 2
m1 = valor//1
valor %= 1
m50 = valor//0.5
valor %= 0.5
m25 = valor//0.25
valor %= 0.25
m10 = valor//0.1
valor %= 0.1
m5 = valor//0.05
valor %= 0.05
valor = round(valor/0.01)
print('NOTAS:')
print(int(n100), 'nota(s) de R$ 100.00')
print(int(n50), 'nota(s) de R$ 50.00')
print(int(n20), 'nota(s) de R$ 20.00')
print(int(n10), 'nota(s) de R$ 10.00')
print(int(n5), 'nota(s) de R$ 5.00')
print(int(n2), 'nota(s) de R$ 2.00')
print('MOEDAS:')
print(int(m1), 'moeda(s) de R$ 1.00')
print(int(m50), 'moeda(s) de R$ 0.50')
print(int(m25), 'moeda(s) de R$ 0.25')
print(int(m10), 'moeda(s) de R$ 0.10')
print(int(m5), 'moeda(s) de R$ 0.05')
print(int(valor), 'moeda(s) de R$ 0.01')
