def is_float(value):
  try:
    float(value)
    return True
  except:
    return False




def leiadinheiro(msg):
   r = input(msg).replace(',','.').strip()
   while not  r.isnumeric() :
       if is_float(r):
           break
       print(f'\033[31mERRO!!! {r.strip()} não é um preço valido\033[m')
       r = input(msg).replace(',','.').strip()
   r = float(r)
   return r

