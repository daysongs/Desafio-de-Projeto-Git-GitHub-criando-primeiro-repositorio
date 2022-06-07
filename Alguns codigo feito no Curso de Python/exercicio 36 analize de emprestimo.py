casa = float(input('Valor da casa: R$'))
s = float(input('Salario do comprador: R$'))
anos = float(input('Qantos anos de financiamento? '))
prestaçao = casa / (anos * 12)
avaliaçao = s * (30/100)
if prestaçao <= avaliaçao:
    print('Para pagar uma casa de R${} em {} anos as prestações serão no valor de R${}\n Emprestimo pode ser concedido'.format(casa,anos,prestaçao))
else:
    print( 'Para pagar uma casa de R${} em {} anos as prestações serão no valor de R${}\n Emprestimo negado'.format(casa, anos, prestaçao))