from datetime import date
nascimento = int(input('ano de nascimento: '))
atual = date.today().year
idade = atual - nascimento
print('O atleta tem {} anos'.format(idade))
if idade <= 9 :
    print('CLASSIFICAÇÃO: MIRIM')
elif 9 < idade <= 14 :
    print('CLASSIFICAÇÃO: INFANTIL')
elif 14 < idade <= 19 :
    print('CLASSIFICAÇÃO: JUNIOR')
elif 19 < idade <= 25:
    print('CLASSIFICAÇÃO: SÊNIOR')
else:
    print('CLASSIFICAÇÃO: MASTER')
