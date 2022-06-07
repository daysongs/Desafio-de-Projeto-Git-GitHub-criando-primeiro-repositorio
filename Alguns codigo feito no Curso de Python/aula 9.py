nome = str(input('digite seu nome')).strip()
print('Analisando seu nome...')
print('seu nome em maiusculo é {}'.format(nome.upper()))
print('seu nome em menusculo é {}'.format(nome.lower()))
print('seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))
print('seu primeiro nome tem {} letras'.format(nome.find(' ')))

