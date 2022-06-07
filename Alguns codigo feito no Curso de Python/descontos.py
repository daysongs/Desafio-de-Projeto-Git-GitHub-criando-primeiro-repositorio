valor=float(input('digite o valor do produto R$'))
desconto= valor*0.05
nvalor=valor-desconto
print(' o produto que custva R${} está com 5% de desconto e vai custar R${:.2f} '.format(valor,nvalor))