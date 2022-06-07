from time import sleep
def contador(t1,t2,dq):
    if dq < 0:
        dq *= -1
    if dq == 0:
        dq = 1
    print('=-'*20)
    print(f'Contagem de {t1} até {t2} de {dq}')

    if t1 < t2:
        cont = t1
        while cont <= t2:
            print(f'{cont}',end=' ')
            cont += dq
            sleep(0.5)
        print()
    else:
        cont = t1
        while cont >= t2:
            print(f'{cont}',end=' ')
            cont -= dq
            sleep(0.5)
        print()
    print('Fim',end=' ')
    print()



#programa principal
contador(1,10,1)
contador(10,1,2)
print('=-'*20)
print('Agora sua vez de pessonalizar')
i = int(input('Inicio: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
contador(i,f,p)
