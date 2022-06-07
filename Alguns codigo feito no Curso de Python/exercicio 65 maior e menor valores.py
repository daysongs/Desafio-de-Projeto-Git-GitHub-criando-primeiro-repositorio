soma = cont = 0
c = 'sS'
maior = menor = 0

while c in 'sS':
    n = float(input('Digite um número: '))
    soma += n
    cont += 1
    if cont ==1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        else:
            menor = n
    c = input('Quer continiuar [S/N]: ').strip().upper()[0]

media = soma / cont
print('você digitou {} números a média foi {} o maior foi {} e o menor foi {}'.format(cont,media,maior, menor))

