from datetime import date
trabalhador = {}
atual = date.today().year
trabalhador['Nome'] = str(input('Nome: '))
nascimeto = int(input('Ano de Nascimento: '))
trabalhador['Idade'] = atual -nascimeto
ctps = int(input('número da carteira de trbalho ( 0 não tem): '))
if ctps == 0:
    trabalhador['CTPS'] = ctps
else:
    trabalhador['CTPS'] = ctps
    contrataçao = int(input('Ano da contratação: '))
    trabalhador['Contratação'] = contrataçao
    trabalhador['Salario'] = float(input('Salario: R$'))
    trabalhador['Aposentadoria'] = (atual - nascimeto) + (atual - contrataçao) + 35
print('=-'*30)
for k , v in trabalhador.items():
    print(f'{k} tem o valor {v}')
