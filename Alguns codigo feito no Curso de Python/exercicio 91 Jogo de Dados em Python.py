from random import randint
from time import sleep
from operator import itemgetter #para colocar os dicionarios em ordem
jogadores = {}
rankik = []
jogadores['Jogador1'] = randint(1,6)
jogadores['Jogador2'] = randint(1,6)
jogadores['Jogador3'] = randint(1,6)
jogadores['Jogador4'] = randint(1,6)
for k , v in jogadores.items():
    print(f'{k} Tirou {v} no dado')
    sleep(1)
rankik = sorted(jogadores.items(), key=itemgetter(1), reverse=True) # coloca o dicionario na oredem decrecente dentro de uma lista
print('=-'*30)
print('  ==  Ranking Dos Jogaderes  ==  ')
for i ,v in enumerate(rankik):
    print(f'   O {i+1}º Lugar foi do {v[0]}.')
    sleep(1)