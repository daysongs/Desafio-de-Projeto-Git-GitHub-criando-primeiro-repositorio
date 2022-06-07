soma = 0
cont = 0
for c in range(1,7):
    n = int(input('digite o {} o valor: '.format(c)))
    if n % 2 == 0:
        cont = cont + 1
        soma = soma + n
print(' a soma de {} número pares é {}'.format(cont,soma))
