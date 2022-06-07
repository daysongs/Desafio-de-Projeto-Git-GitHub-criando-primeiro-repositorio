n = (int(input('Digite um valor')),int(input('Digite um valor')),
     int(input('Digite um valor')),int(input('Digite um valor')),
     int(input('Digite um valor')))
print(f'Você digitou os valores: {n}')
print(f'o valor 9 apareceu {n.count(9)} vezes')
if 3 in n :
    print(f'o valor 3 apareceu a primeira vez na posição {n.index(3)+1}')
else:
    print(' O valor 3 não foi digitado')
print('Os valores pares digitados foram: ',end='')
for num in n:
    if num % 2 == 0:
        print(num,end=' ')
   
