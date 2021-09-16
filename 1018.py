valor1 = int(input())
valor = valor1
n100 = 0
n50 = 0
n20 = 0
n10 = 0
n5 = 0
n2 = 0
n1 = 0
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
n1 = valor//1
valor %= 1
print(valor1)
print(n100, 'nota(s) de R$ 100,00')
print(n50, 'nota(s) de R$ 50,00')
print(n20, 'nota(s) de R$ 20,00')
print(n10, 'nota(s) de R$ 10,00')
print(n5, 'nota(s) de R$ 5,00')
print(n2, 'nota(s) de R$ 2,00')
print(n1, 'nota(s) de R$ 1,00')
