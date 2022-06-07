from random import randint
print('''Sou se computador...
Acabei de pensar em um número entre 0 e 10
séra que vc que você consegue adivinhar qual foi?''')
computador = randint(0,10)
jogador = int(input(' qual o seu pailpite? '))
c = 1
while not jogador == computador:
    c += 1
    if jogador < computador :
        jogador = int(input('''Mais... Tente novamente
        Qual é seu pailpite'''))
    else:
        jogador = int(input('''menos... Tente novamente
        Qual é seu pailpite'''))

print('acerotu com {} tentativas Parabens!'.format(c))
