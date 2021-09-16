idade = int(input())
mes, dia, ano = 0, 0, 0
ano = idade//365
idade %= 365
mes = idade//30
dia = idade % 30
print(ano, 'ano(s)')
print(mes, 'mes(es)')
print(dia, 'dia(s)')
