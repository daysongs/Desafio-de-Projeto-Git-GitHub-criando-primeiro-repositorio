from time import sleep
def maior(*num):
    cont = maior = 0
    print('=-'*30)
    print('Analizando os valores passado.....')
    for c in num:
        print(c,end=' ')
        sleep(0.5)
        if cont == 0:
            maior = c
        else:
            if c > maior:
                maior = c
        cont += 1
    print(f'Ao todo foram analizados {cont} valores.',end=' ')
    print()
    print(f'O maior valor informado foi {maior}')


#programa principal
maior(2,3,4,5,6,9)
maior(0,2,6)
maior(0,4)
maior(7)
maior()