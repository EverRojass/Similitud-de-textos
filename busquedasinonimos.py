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
 

