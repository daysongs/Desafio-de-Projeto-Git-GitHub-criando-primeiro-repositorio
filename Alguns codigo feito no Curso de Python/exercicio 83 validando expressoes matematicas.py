exp = str(input('Digite uma espressão: '))
pilha = []
for simb in exp:
    if simb in '(' :
        pilha.append('(')
    elif simb in ')' :
        if len(pilha) > 0 :
            pilha.pop()
        else:
            pilha.append(')')
if len(pilha) == 0 :
    print('Sua expressão esta correta')
else:
    print('Sua exprssão esta invalida')