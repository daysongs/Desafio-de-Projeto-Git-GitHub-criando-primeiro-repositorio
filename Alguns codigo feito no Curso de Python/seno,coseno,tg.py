import math

ag = float(input('digite um ângulo:'))
seno = math.sin(math.radians(ag))
cos = math.cos(math.radians(ag))
tg = math.tan(math.radians(ag))
print('o ângulo de {} tem o seno de {:.2f}'.format(ag,seno))
print('o ângulo de {} tem o cosseno de {:.2f}'.format(ag,cos))
print('o ângulo de {} tem a tangente de {:.2f}'.format(ag,tg))

