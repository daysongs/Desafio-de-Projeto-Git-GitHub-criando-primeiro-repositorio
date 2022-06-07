def is_float(value):
  try:
    float(value)
    return True
  except:
    return False




def leiadinheiro(msg):
   r = input(msg).replace(',','.')
   while not  r.isnumeric() :
       if is_float(r):
           break
       print(f'\033[31mERRO!!! {r.strip()} não é um preço valido\033[m')
       r = input(msg).replace(',','.')
   r = float(r)
   return r

m = leiadinheiro('Digite um preço: ')
print(m)
print(is_float('abc'))