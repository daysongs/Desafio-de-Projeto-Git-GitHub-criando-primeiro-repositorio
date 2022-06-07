print('='*30)
print('{:^30}'.format(' Banco CV '))
print('='*30)
saque = int(input('Qanto você quer sacar'))
total = saque
ced = 50
tced = 0
while True:
    if total >= ced:
        total -=ced
        tced += 1
    else:
        if tced > 0:
            print(f'Total de {tced} de cedulas de R${ced}')
        if ced == 50:
            ced = 20
        elif ced ==20 :
            ced = 10
        elif ced == 10:
            ced = 5
        elif ced == 5 :
            ced = 1
        tced = 0
        if total == 0 :
            break
print('='*30)
print('Volte sempre!!')


