km=float(input('quantos Km foram pecorrido? '))
d=float(input('quanto dias você ficou com o carro?'))
p= (km*0.15) + (d*60)
print('o total a pagar é de R${:.2f}'.format(p))