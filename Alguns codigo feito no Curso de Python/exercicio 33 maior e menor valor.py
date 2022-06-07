n1 = int(input('digite um número: '))
n2 = int(input('digite o segundo número: '))
n3 = int(input('digite o terceiro nùmero: '))
# verifica quem é o menor
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
print('menor valor digitado foi {}'.format(menor))
# verifica quem é o mairo
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
print('o maior valor foi {}'.format(maior) )