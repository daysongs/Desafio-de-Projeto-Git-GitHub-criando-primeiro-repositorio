lista = []
par = []
impar = []
while True:
    lista.append(int(input('Digite um valor: ')))
    op = input('Quer continuar [S/N]: ').strip().upper()[0]
    if op in 'nN':
        break
for cp in range(0,len(lista)) :
    if lista[cp] % 2 == 0:
        par.append(lista[cp])
    else:
        impar.append(lista[cp])
print('-='*30)
print(f'A lista completa é: {lista}')
print(f'A lista de números Pares é: {par}')
print(f'A lista de número Impares é: {impar}')