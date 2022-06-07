'''co = float(input('comprimento do cateto oposto:'))
ca = float(input('comprimento do cateto adejacente:'))
h = (co**2+ca**2)**(1/2)
print('o co vale {}cm o ca vale {}cm logo a hipotenusa é de {}cm'.format(co,ca,h))'''
import math
co = float(input('compimento do cateto oposto:'))
ca = float(input('comprimento di cateto adejacente:'))
h = math.hypot(co,ca)
print(' a hipotenusa vale {}'.format(h))
