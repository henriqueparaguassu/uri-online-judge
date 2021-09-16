vetor_1 = input().split()
peso = [2, 3, 4, 1]
vetor = []
for i in range(len(vetor_1)):
    vetor.append((float(vetor_1[i]))*peso[i])
notas = sum(vetor)/sum(peso)
print('Media:', '%.1f' % notas)
if notas >= 7.0:
    print('Aluno aprovado.')
elif notas < 5.0:
    print('Aluno reprovado.')
elif (notas >= 5.0) and (notas < 7.0):
    print('Aluno em exame.')
    exame = float(input())
    print('Nota do exame:', exame)
    notas = (notas + exame)/2
    if notas >= 5.0:
        print('Aluno aprovado.')
        print('Media final:', '%.1f' % notas)
    elif notas < 5.0:
        print('Aluno reprovado.')
        print('Media final:', '%.1f' % notas)
