print('Geradoar de PA  ')
print('=-='*10)
t = int(input('Primeiro termo: '))
r = int(input('Razão: '))
termo = t
cont = 1
mais = 10
total = 0
while mais != 0:
    total = total + mais
    while cont <= total  :
        print('{}'.format(termo), end=' → ')
        termo += r
        cont +=1
    print('pausa')
    mais = int(input('Qantos termos você quer mostra mais'))
print(' ao total sua PA teve {} termos'.format(total))