from math import sqrt
print('Para caucular suas raizes da equação de segundo grau digite a seguir os valor de:')
a = float(input('Valor de a: '))
b = float(input('Valor de b: '))
c = float(input('Valor de c: '))
d = b**2 - 4*a*c
if d > 0:
    x1 = (-b + sqrt(d))/(2 * a)
    x2 = (-b - sqrt(d))/(2 * a)
    if x1 > x2:
        print('as raízes da equção são {} e {}'.format(x2,x1))
    else:
        print('as raízes da equção são {} e {}'.format(x1, x2))
elif d == 0:
    x = -b/(2*a)
    print(' a raiz desta equação é {}'.format(x))
else:
    print('esta equação não possui raízes reias.')
