cont = soma = n = 0
n = int(input('Digite um número [999 para sair]: '))
while n != 999:
    soma += n
    cont += 1
    n = float(input('Digite um número [999 para para]: '))
print('Você digitou {} números e a soma entre eles é {}'.format(cont,soma))