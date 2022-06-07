alunos = []

while True:
    nome = input('Digite o nome do aluno: ').strip()
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))
    media = (n1 + n2) / 2
    alunos.append([nome, [n1, n2], media])
    op = str(input('Quer continuar [S/N]')).strip().upper()[0]
    if op in 'N':
        break
print('=-'*30)
print(f"{'No.':<4}{'NOME':<10}{'Média':>8}")
for c, a in enumerate(alunos):
    print(f"{c:<4}{a[0]:<10}{a[2]:>8.1f}")
while True:
    print('-'*35)
    op = int(input(('Qual aluno você quer ver:  (999 para sair)')))
    if op == 999:
        break
    if op <= len(alunos) -1 :
        print(f'As noatas de {alunos[op][0]} são: {alunos[op][1]}')
print('finalizado')
