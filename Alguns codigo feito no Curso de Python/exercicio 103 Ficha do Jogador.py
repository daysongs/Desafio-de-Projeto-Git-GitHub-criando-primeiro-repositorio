def ficha(g=0,n='desconhecido'):
    return f'O Jogador {n} fez {g} gols'

#programa principal
nome = str(input('Nome do jogador: '))
gols = str(input('Números de gols: '))
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0
if nome.strip() == '':
    nome = 'desconhecido'

print(ficha(gols,nome))