frase = str(input('Digite uma frase: ')).strip().upper()
palavra = frase.split()
junto = ''.join(palavra)
inverso = junto[::-1]
'''for letra in range(len(junto)-1,-1,-1):
    inverso = inverso + junto[letra]'''
print('o inverso de {} é {}'.format(junto,inverso))
if inverso == junto:
    print(' temos um palimedro')
else:
    print('não temos um palimedro')
