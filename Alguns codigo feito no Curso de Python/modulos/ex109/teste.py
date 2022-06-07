from ex109 import moedas
num = float(input('Digite um valor: R$'))
print(f'A metade de {moedas.moeda(num)} é {moedas.metade(num,True)} ')
print(f'O dobro de {moedas.moeda(num)} é {moedas.dobro(num,True)}')
print(f'Aumentando 10% em {moedas.moeda(num)} temos {moedas.aumentar(num, 10,True)}')
print(f'diminuindo 10% em {moedas.moeda(num)} temos {moedas.diminuir(num, 10,True)}')


