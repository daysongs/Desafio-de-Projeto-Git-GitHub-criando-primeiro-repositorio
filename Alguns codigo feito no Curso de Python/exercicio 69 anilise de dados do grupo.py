print('-'*20)
print('Cadastre uma pessoa')
print('-'*20)
mais18 = homens = mulheresmenos20 = 0
while True:
    idade = int(input('IDADE: '))
    sexo = ' '
    while not sexo in 'MF':
        sexo = str(input('SEXO: [M/F]')).strip().upper()[0]
    op = ' '
    if idade >= 18 :
        mais18 += 1
    if sexo == 'M'  :
        homens += 1
    if idade < 20 and sexo =='F':
        mulheresmenos20 += 1
    while not op in 'SN':
        op = str(input('Quer continuar? [S/N] :')).strip().upper()[0]
    if op == 'N':
            break
print(f'Ao todo temos {mais18} pessoas com mais de 18 anos ')
print(f'Ao todo temos {homens} homens cadastrados')
print(f'Ao todo temos {mulheresmenos20} mulheres com menos de 20 anos casdastrada')





