times = ('Flamengo','Santos','Palmeiras','Gremio','Athetlico-PR',
         'São Paulo','Internacional','Coritinhas','Fortaleza',
         'Goiás','Bhaia','Vasco da Gama','Atlético-MG','Fluminense',
         'Boatafogo','Ceará','Cruzeiro','CSA','Chapecoence','Avai')
print('-=-'*30)
print(f'Lista de times Brasileirão: {times}')
print('-=-'*30)
print(f'Os 5 primeiros são: {times[:6]}')
print('-=-'*30)
print(f'Os 4 ultomos são: {times[15:]}')
print('-=-'*30)
print(f'Times em ordem alfabetica: {sorted(times)}')
print('-=-'*30)
print(f"A chapecoense esta na {times.index('Chapecoence')+1}ª posição ")