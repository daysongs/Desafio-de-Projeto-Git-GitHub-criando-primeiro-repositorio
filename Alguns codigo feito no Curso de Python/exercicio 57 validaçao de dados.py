sexo = str(input('Informe seu se sexo [M/F]: ')).strip().upper()[0]
while sexo not in 'MF' :
    print('dados invalidos ')
    sexo = str(input('digite novamente')).strip().upper()[0]
print('dados registrado com sucesso')