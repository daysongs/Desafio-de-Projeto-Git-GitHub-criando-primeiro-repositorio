palavras = ('agua','azul','camarao','manga')
for p in palavras:
    print(f'\n na palavra {p} temos as vogais ',end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra,end=' ')