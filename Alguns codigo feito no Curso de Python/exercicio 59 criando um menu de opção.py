from time import sleep
v1 = int(input('Primeiro valor: '))
v2 = int(input('segundo valor: '))
op = 0
while not op == 5 :
    print('''    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novo número
    [ 5 ] sair do programa''')
    op = int(input('→→→→→→ Qual sua Opção? '))
    if op == 1 :
        print('a soma entre {} + {} = {}'.format(v1,v2,v1+v2))
    elif op == 2 :
        print('a multiplicação entre {} x {} = {}'.format(v1,v2,v1*v2))
    elif op == 3 :
        if v1 > v2 :
            print(' o primeiro valor {} é maior que o segundo valor {}'.format(v1,v2))
        else:
            print('o segundo valor {} é maior que o o pirmeiro {}'.format(v2,v1))
    elif op == 4 :
        print('→→→→→→ Qais são os números novamente?')
        v1 = int(input('Primeiro valor: '))
        v2 = int(input('Segundo valor: '))
    elif op != 5 and op > 4 :
        op = int(input('Opção invalida tente novamente: '))
print(' saindo do program....')
sleep(2)
print('programa encerrado')

