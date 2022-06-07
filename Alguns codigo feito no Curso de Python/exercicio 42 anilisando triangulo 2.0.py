reta1 = float(input('Medida do primeiro seguimento de reta: '))
reta2 = float(input('Medida do segundo seguimento de reta: '))
reta3 = float(input('Medida do terceiro seguimento de reta: '))
if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta2:
    print('pode forma um triangulo', end='')
    if reta1 == reta2 == reta3:
        print(' EQILÁTERO')
    elif reta1 != reta2 != reta3 != reta1 :
        print(' ISOCELES')
    else:
        print(' ESCALENO')

else:
    print('Não pode ser formado nenhum triangulo tente outro seguimentos de reta')
