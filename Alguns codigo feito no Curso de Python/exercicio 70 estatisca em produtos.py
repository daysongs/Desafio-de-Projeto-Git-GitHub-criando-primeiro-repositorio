totalgasto = quatcustamais1000 = maisbarato =cont = 0
nomemaisbarato = ''
print('-'*20)
print('Loja Super baratão')
print('-'*20)
while True:
    nomeproduto = str(input('Nome do Produtudo: ')).strip()
    p = float(input('Preço R$'))
    op = ' '
    totalgasto += p
    cont += 1
    if cont == 1:
        maisbarato = p
    else:
        if p < maisbarato:
            maisbarato = p
            nomemaisbarato = nomeproduto
    if p < maisbarato:
        maisbarato = p
        nomemaisbarato = nomeproduto
    if p > 1000 :
        quatcustamais1000 += 1
    while op not in 'SN':
        op = str(input('Quer continuar: [S/N]')).strip().upper()[0]
    if op == 'N':
        break
print(f'O total da compra foi R$ {totalgasto:.2f}')
print(f'Temos {quatcustamais1000} produtos que custam mais de R$ 1000,00')
print(f'O produto mais barato foi {nomemaisbarato} que custa R${maisbarato:.2f}')