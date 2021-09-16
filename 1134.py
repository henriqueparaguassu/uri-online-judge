alcool, gas, diesel, a = 0, 0, 0, 0
while a != 4:
    a = int(input())
    if a == 1:
        alcool += 1
    if a == 2:
        gas += 1
    if a == 3:
        diesel += 1
print('MUITO OBRIGADO')
print('Alcool:', alcool)
print('Gasolina:', gas)
print('Diesel:', diesel)
