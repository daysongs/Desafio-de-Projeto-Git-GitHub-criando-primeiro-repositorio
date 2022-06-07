extenso = ('zero','um','dois','tres','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','catorze','quinze','dizesseis','dezessete','dezoito','dezenove','vinte')
n = int(input('Digite um número entre 0 e 20:  '))
while  n > 20:
    n = int(input('Tente novamente, digite um número entre 0 e 20: '))
print('Você digitou o número {}'.format(extenso[n]))