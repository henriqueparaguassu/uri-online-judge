# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''

renda = float(input())

if (renda <= 2000):
    print("Isento")

if (renda > 2000) and (renda <= 3000):
    final = ((renda - 2000) * 0.08)
    print("R$", "%.2f" % final)

if (renda > 3000) and (renda <= 4500):
    final = ((renda - 2000 - (renda - 3000)) * 0.08) + ((renda - 3000) * 0.18)
    print("R$", "%.2f" % final)

if (renda > 4500):
    final = ((renda - 2000 - (renda - 3000)) * 0.08) + \
        ((renda - 3000 - (renda - 4500)) * 0.18) + ((renda - 4500) * 0.28)
    print("R$", "%.2f" % final)
