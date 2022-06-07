# Equipe: Dayvson Gonçalves da Silva
# Renato
def digitetemporada():
    t = input('Quantas temporadas essa série possui? ')
    while not t.isnumeric():
        print('\033[31mErro Tente novamente\033[m')
        t = input('Quantas temporadas essa série possui? ')


sereis_favoritas = ['The big theory','How I Met Your Mother','Friends','Dexter','Atypical'
    ,'Young Sheldon','Supernatural','Sherlock','Chuck','O Mentalista']
temporadas = [12,9,10,8,3,3,15,4,5,7]
ts = digitetemporada()
