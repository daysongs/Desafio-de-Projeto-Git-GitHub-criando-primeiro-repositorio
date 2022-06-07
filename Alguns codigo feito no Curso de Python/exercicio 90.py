alunos = {}
alunos['nome'] = str(input('Nome do aluno: '))
alunos['média'] = float(input('Média do aluno: '))
print('-'*30)
if alunos['média'] < 5 :
    alunos['situação'] = 'Reprovado'
elif 5 <= alunos['média'] < 7 :
    alunos['situação'] = 'Recuperação'
else:
    alunos['situação'] = 'Aprovado'
for i , v in alunos.items():
    print(f'{i} é igual {v}')