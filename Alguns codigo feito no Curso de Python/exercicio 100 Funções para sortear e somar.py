from random import randint
'''def valores(*valores):
    lista = []
    soma = 0
    print('Sortiando 5 valores em uma lista: ',end=' ')
    for v in valores:
        print(v,end=' ')
        lista.append(v)
        if v % 2 == 0:
            soma += v
    print()
    print(f'Somando os valores pares de {lista}, temos {soma}')




#programa principal
valores(randint(1,10),randint(1,10),randint(1,10),randint(1,10),randint(1,10))'''
def sorteia(lista):
    print('Sorteando 5 valores da lista: ',end=' ')
    for v in range(0,5):
        n = randint(0,10)
        lista.append(n)
        print(f'{n}',end=' ')
    print()
def somapar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'Somando os valores da lista {lista}, temos {soma}')

#programa principal
número = []
sorteia(número)
somapar(número)
