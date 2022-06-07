pessos = []
cadastros = {}
med = 0
while True:
    cadastros.clear()
    cadastros['Nome'] = str(input('Nome: ')).strip()
    cadastros['Idade'] = int(input('Idade: '))
    cadastros['Sexo'] = str(input('Sexo [M/F]: ')).strip().upper()[0]
    while cadastros['Sexo'] not in 'MF':
        print('ERRO!! APENAS RESPONDA COM M OU F')
        cadastros['Sexo'] = str(input('Sexo [M/F]: ')).strip().upper()[0]
    op = str(input('Quer continuar [S/N]: ')).strip().upper()[0]
    while op not in 'SN':
        print('ERRO!!! APENAS RESPONDA COM S OU N')
        op = str(input('Quer continuar [S/N]: ')).strip().upper()[0]
    pessos.append(cadastros.copy())
    med += cadastros['Idade']
    if op in 'nN' :
        break
media = med / len(pessos)
print(f'Ao todo foram cadastradas {len(pessos)} pessoas')
print(f'A média de iadade é {media:5.2f}')
print(' As mulheres cadastradas foram ',end=' ')
for p in pessos:
    if p['Sexo'] == 'F':
        print(f'{p["Nome"]}',end=' ')
print()
print('A lsita de pessoas que está acima da média é: ')
for p in pessos:
    if p['Idade'] >= media:
        print('  ',end='')
        for v , i in p.items():
            print(f'{v} = {i}',end=' ')
        print()
print('←← ENCERRADO →→')
