n = int(input('digite um número inteiro: '))
print('Escolhas umas das bases para converção')
print('[ 1 ] converter para BINARIO')
print('[ 2 ] converter para OCTAL')
print('[ 3 ] converter para HEXADECIMAL')
o = int(input('sua opção: '))
if o == 1 :
    print('{} convertido para binario é igual {}'.format(n,bin(n)[2:]))
elif o == 2 :
    print('{} convertido para octal é igual {}'.format(n,oct(n)[2:]))
elif o == 3 :
    print('{} convertido para hexadecimal é igual {}'.format(n,hex(n)[2:]))
else:
    print('opção invalida tente novamente')