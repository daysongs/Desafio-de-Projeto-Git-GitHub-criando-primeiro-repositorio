from random import randint
n = (randint(0,100),randint(0,100),randint(0,100),randint(0,100),randint(0,100))
print('Os valores sorteados foram: ',end='')
for nun in n:
    print(nun,end=' ')
print(f'\nO maior valor foi {max(n)}')
print(f'O menor valor foi {min(n)}')
