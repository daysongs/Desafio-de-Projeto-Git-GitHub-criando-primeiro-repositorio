dados = []
pessoa = []
cont = maiorp = menorp = 0
while True:
    dados.append(str(input('Nome: ')).strip())
    dados.append(float(input('Peso: ')))
    cont += 1
    if len(pessoa) == 0:
        maiorp = menorp = dados[1]
    else:
        if dados[1] > maiorp :
            maiorp = dados[1]
        if dados[1] < menorp :
            menorp = dados[1]
    pessoa.append(dados[:])
    dados.clear()
    op = str(input('Quer continuar [S/N]: ')).strip().upper()[0]
    if op in 'N':
        break
print(f'Foram cadastradas {cont} pessoas')
print(f' O maior peso foi {maiorp:.1f}Kg. Peso de ',end='')
for p in pessoa:
    if p[1] == maiorp:
        print(f'[{p[0]}] ',end='')
print()
print(f'O menor peso foi {menorp:.1f}Kg. peso de ',end='')
for p in pessoa:
    if p[1] == menorp:
        print(f'[{p[0]}]',end='')
