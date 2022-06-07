import moedas
num = float(input('Digite um valor: R$'))
print(f'A metade de R${num} é R${moedas.metade(num)}')
print(f' O dobro de R${num} é R${moedas.dobro(num)}')
print(f'Aumentando R%{num} em 10% temos R${moedas.aumentar(num, 10)}')
print(f'diminuindo R${num} em 10% temos R${moedas.diminuir(num, 10)}')
