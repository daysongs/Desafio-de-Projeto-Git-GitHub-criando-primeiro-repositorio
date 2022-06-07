print('=-='*20)
print('Calculando seu Indice de Massa Corporal')
print('=-='*20)
peso = float(input(' Digite seu peso em Kg: '))
altura = float(input('Digite sua altura em metros'))
imc = peso / altura ** 2
print('O IMC dessa pessoa é {:.2f}'.format(imc))
if imc < 18.5:
    print( 'ABAIXO DO PESO NORMAL')
elif 18.5 < imc <= 25:
    print('PESO IEDEAL')
elif 25 < imc <= 30 :
    print('SOBREPESO')
elif 30 < imc <= 40:
    print('OBESIDADE')
else:
    print('OBESIDADE MORBIDA')
