partida = {}
gols = []
time = []
total = 0
while True:
    partida.clear()
    gols.clear()
    partida['nome'] =str(input('Nome do jogador: '))
    np = int(input('Qantas partidas foram jogadas: '))
    for c in range(1,np+1):
         gols.append(int(input(f'Qantos gols na partida {c}: ')))
    partida['gols'] = gols[:]
    partida['total'] = sum(gols)
    time.append(partida.copy())
    op = str(input('Quer continuar [S/N] :')).strip().upper()[0]
    while op not in 'SN':
        print('Opção invalida apenas responda com S ou N')
        op = str(input('Quer continuar [S/N] :')).strip().upper()[0]
    if op in 'nN':
        break
print('=-'*40)
print(f'{"cod":<10} {"Nome":<8} {"Gols":>12} {"Total":>10}')
print('-'*40)
for c , v  in enumerate(time):
    print(f'{c:<10} ',end='')
    for p in v.values():
        print(f'{str(p):<15}',end='')
    print()
print('-'*40)
while True:
    op = int(input('Mostrar os Dados de Qual Jogadoro (999 para sair): '))
    if op == 999:
        break
    if op >= len(time):
        print(f'Erro não existe o jogador com o cod {op}')
    else:
        print(f'--- LEVANTAMENTO DO JOGADOR {time[op]["nome"]}')
        for i, g in enumerate(time[op]['gols']):
            print(f'   No jogo {i+1} fez {g} gols')
print('-'*40)
print('←←← FINALIZADO →→→')

