print('Geradoar de PA  ')
print('=-='*10)
t = int(input('Primeiro termo: '))
r = int(input('Razão: '))
termo = t
cont = 1
while cont <= 10  :
    print('{}'.format(termo), end=' → ')
    termo += r
    cont +=1
print('Fim')