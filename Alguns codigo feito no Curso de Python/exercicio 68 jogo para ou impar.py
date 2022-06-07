from random import randint
ints = ('Par','impar')
print('-'*30)
print('vamos jogar par ou impar: ')
print('-'*20)
cont = 0
while True:
    jogador = int(input('Digite um valor'))
    computado = randint(0,10)
    op = str(input(' Qual você quer [P/I]: ')).strip().upper()[0]
    par = (computado + jogador) % 2
    while op not in 'PI':
        op = str(input(' Qual você quer [P/I]: ')).strip().upper()[0]
    print(f'Jogador jogou {jogador} e computador jogou {computado}. Toatal {jogador + computado} deu {ints[par]}')
    if par == 0 and op in 'P':
        print('você venceu!!!')
    else:
        if par != 0 and op in 'I':
            print('Você venceu!! ')
        else:
            print('Eu venci!!!')
            break
    cont += 1
    print('vamos jogar novamente...')
print(f'GAMER OVER você venceu {cont} vez ')




