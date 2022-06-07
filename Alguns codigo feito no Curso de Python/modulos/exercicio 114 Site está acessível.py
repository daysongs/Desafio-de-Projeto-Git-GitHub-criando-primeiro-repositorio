import urllib
import urllib.request
try:
    site = urllib.request.urlopen('https://www.google.com.br/')
except(urllib.error.URLError):
    print('O site esta inacessivel no momento')
else:
    print('conceguimos acessar o site')