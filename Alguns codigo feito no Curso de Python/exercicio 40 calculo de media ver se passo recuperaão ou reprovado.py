nota1 = float(input('Digite a primeira nota do aluno:  '))
nota2 = float(input('Digite a segunda nota do aluno: '))
media = (nota1 + nota2) / 2
print('A media do aluno foi {:.2f}'.format(media))
if media < 5:
    print('\33[0;31nREPROVADO\33[n'.format(media))
elif media >= 5 and media < 7:
    print('\33[0;33nRECUPERAÇÃO\33[n')
else:
    print('\33[0;32nAPROVADO\33[n')