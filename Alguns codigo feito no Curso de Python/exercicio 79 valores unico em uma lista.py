lista = []
while True:
    n = int(input('Digite um número: '))
    if n not in lista:
        lista.append(n)
        print('Valor adicionado com sucesso')
    else:
        print('Valor duplicado não vou adicinar')
    op = str(input('Quer continuar [S/N]: ')).strip().upper()[0]
    if op in 'N':
        break

lista.sort()
print(f'Os valores adicionado foram {lista}')

