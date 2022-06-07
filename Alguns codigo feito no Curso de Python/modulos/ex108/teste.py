from ex108 import moedas
num = float(input('Digite um valor: R$'))
print(f'A metade de {moedas.moeda(num)} é {moedas.moeda(moedas.metade(num))}')
print(f'O dobro de {moedas.moeda(num)} é {moedas.moeda(moedas.dobro(num))}')
print(f'Aumentando {moedas.moeda(num)} em 10% temos {moedas.moeda(moedas.aumentar(num, 10))}')
print(f'diminuindo {moedas.moeda(num)} em 10% temos {moedas.moeda(moedas.diminuir(num, 10))}')


