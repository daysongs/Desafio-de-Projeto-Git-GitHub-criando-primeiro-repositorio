n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a sehunda nota: '))
m = (n1 + n2)/2
print('Sua media foi {: 1f}'.format(m))
if m >= 6.0:
    print('Aprovado, Parabens')
else:
    print('Reprovado, Estude mais')
