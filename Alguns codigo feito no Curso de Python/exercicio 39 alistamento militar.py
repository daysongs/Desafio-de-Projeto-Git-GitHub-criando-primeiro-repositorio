from datetime import date
nascimento = int(input('Qual ano você nasceu?'))
atual = date.today().year
idade = atual - nascimento
print('Quem nasceu em {} tem {} anos em {}'.format(nascimento,idade,atual))
if idade < 18 :
    saldo = 18 - idade
    ano = saldo + atual
    print('ainda faltam {} para você se alistar\n Você tem que se alistar no ano {}'.format(saldo,ano))
elif idade == 18 :
    print('Você tem que se alistar IMEDIATAMENTE')
else :
    saldo = idade - 18
    ano = atual - saldo
    print('você deveria te se alitado a {} anos atrais\nno ano de {}'.format(saldo,ano))