print('='*20 + ' Lojas Dayvson '+ '='*20)
valor = float(input('Digite o valor do produto'))
print('''Escolha a forma de pagamento:
[ 1 ] à vista dinheiro/cheque
[ 2 ] À vista no cartão
[ 3 ] Até 2x no cartão
[ 4 ] 3x ou mais no cartão''')
op = int(input(' Escolha a forma de pagamento: '))
if op == 1 :
    desconto = valor - (valor*10/100)
    print('sua compra de R${:.2f} vai custar R${:.2f}  '.format(valor,desconto))
elif op == 2 :
    desconto = valor - ( valor*5/100)
    print('sua compra de R${:.2f} vai custar R${:.2f}'.format(valor,desconto))
elif op == 3 :
    p = int(input('Qauntas parcelas:'))
    m = valor/p
    print('sua compra será parcelada em {}x de R${:.2f} sem juros'.format(p,m))
elif op == 4 :
    p = int(input('Quantas parcelas'))
    vp = valor + (valor*20/100)
    m = vp / p
    print('''    sua compra sera parcelada em {}x de R${:.2f} com juros
    sua compra de R${:.2f} vai custar R${:.2f} no final'''.format(p,m,valor,vp))
else:
    print('opção invalida tente novamente')