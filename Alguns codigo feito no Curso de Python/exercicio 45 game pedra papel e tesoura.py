from random import randint
from time import sleep
itens = ('pedra','paepl','tesoura')
computador = randint(0,2)
print('''Sua opção:
[ 0 ] pedra
[ 1 ] papel
[ 2 ] tesoura''')
jogador = int(input('Qual a sua jogada'))
sleep(1)
print('JO')
sleep(1)
print('KEM')
sleep(1)
print('PO!!!')
print('=-='*11)
print('o computador jogou {}'.format(itens[computador]))
print('O jogador jogou {}'.format(itens[jogador]))
print('=-='*11)
if computador == 0:
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('jogador venceu')
    elif jogador == 2:
        print('computador venceu')
    else:
        print('JOGADA INVALIDA')
elif computador == 1:
    if jogador == 0:
        print('computador venceu')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('jogador venceu')
    else:
        print('Jogada invalida')
elif computador == 2:
    if jogador == 0 :
        print('jogador venceu')
    elif jogador == 1 :
        print('computador venceu')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('jogada invalida')





