print('-=-'*20)
print('analisandor de triangulos')
print('-=-'*20)
r1 = float(input('primeiro seguimento: '))
r2 = float(input(' segundo segumento: '))
r3 = float(input('terceiro segumento: '))
if r1 < (r2+r3) and r2 < r3 + r1 and r3 < r1 + r2 :
    print('pode ser formado um triangulo')
else:
    print('não pode ser feito um triangulo')