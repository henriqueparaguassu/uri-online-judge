# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''
senha = 0

while senha != 2002:
    senha = int(input())
    if senha == 2002:
        print("Acesso Permitido")
        break
    else:
        print("Senha Invalida")
