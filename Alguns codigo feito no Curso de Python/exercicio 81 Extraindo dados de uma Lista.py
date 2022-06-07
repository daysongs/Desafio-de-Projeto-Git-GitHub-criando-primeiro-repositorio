lista = []
while True:
    lista.append(int(input('Digite um Valor: ')))
    op = str(input('Quer continuar [S/N]: ')).strip().upper()[0]
    if op in 'N' :
        break
print(f'Você digitou {len(lista)} elementos')
lista.sort(reverse=True)
print(f'Os números em oredem decrescente são {lista}')
if 5 in lista:
    print('O valor 5 faz parte da lista')
else:
    print('O valor 5 não foi encontrado')

