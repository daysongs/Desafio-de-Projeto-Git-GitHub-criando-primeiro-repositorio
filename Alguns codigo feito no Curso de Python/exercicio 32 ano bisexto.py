from datetime import date
ano = int(input('que ano vc quer analizar? Coloque 0 para analizar o ano atual '))
if  ano == 0:
    ano = date.today().year # essa função pega o ano atual da maquina
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é BISSEXTO'.format(ano))
else:
    print('O ano {} não é BISSEXTO'.format(ano))
