salario = float(input('digite o salario atual do fucionario: '))
if salario <= 1250 :
    aumento = salario + (salario*(15/100))
else:
    aumento = salario + (salario*(10/100))
print('Seu fucinario que recebia R${:.2f} passa a receber R${:.2f}'.format(salario,aumento))