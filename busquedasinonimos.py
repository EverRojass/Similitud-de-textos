# Búsqueda de sinónimos de una palabra.
# Autor Everardo Morales Rojas
# Universidad del Mar campus Puerto Escondido.
# 10-10-2023

# - Para uso correcto se requiere haber instaldo las librerías siguientes:

import requests
from bs4 import BeautifulSoup

url='https://www.wordreference.com/sinonimos/'
palabra='tecla'
buscar=url+palabra
resp=requests.get(buscar)
soup=BeautifulSoup(resp.text,features="html.parser")

try:
    lista=soup.find(class_='trans esp clickable')
    sino=lista.find('li')
    print (sino.next_element)
except:
     print('Error')
 

