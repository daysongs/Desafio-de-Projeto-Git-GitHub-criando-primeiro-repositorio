nome = str(input('Digite seu nome cimpleto: ')).strip()
print('muito prazer em te conhecer!')
sp = nome.split()
print('Seu primeiro nome é {} '.format(sp[0]))
print('Seu ultimo Nome é {} '.format(sp[len(sp)-1]))