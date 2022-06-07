def votar(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    print(f'Com {idade} anos ',end=' ')
    if idade <= 15:
        return 'Não vota'
    elif 15 < idade < 18 or idade > 65:
        return  'Voto opicional'
    elif 18 <= idade <= 65:
        return f'Voto obrigatorio'


#programa principal
r = int(input('Que ano você nasceu? '))
print(votar(r))
