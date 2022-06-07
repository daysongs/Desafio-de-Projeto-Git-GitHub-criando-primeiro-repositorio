cont = 0
while True:
    tb = int(input('Qeer ver a tabuada de qual valor? '))
    if tb < 0:
        break
    print('=-='*20)
    for c in range(0, 11):
        print('{} x {} = {}'.format(tb, c, tb * c))
    print('=-=' * 20)
print('Programa de tabuada encerrado vote sempre')
