print('='*30)
print('     10 termos de uma PA')
print('='*30)
t = int(input('Digite o primeiro termo: '))
r = int(input('Razão: '))
for c in range(t,11,r):
    print(c,end=' → ')
print ('acabou  ')