partida = {}
gols = []
total = 0
partida['nome'] =str(input('Nome do jogador: '))
np = int(input('Qantas partidas foram jogadas: '))
for c in range(1,np+1):
    gp = int(input(f'Qantos gols na partida {c}: '))
    total += gp
    gols.append(gp)
partida['gols'] = gols[:]
partida['total'] = total
print('=-'*30)
print(partida)
print('=-'*30)
for k , v in partida.items():
    print(f'No campo {k} tem o valor {v}')
print('=-'*30)
print(f'O joador {partida["nome"]}')
for c, v in enumerate(gols):
    print(f'   → Na partida {c+1}, Fez {v}. ')
print(f'Foi um total de {total}')