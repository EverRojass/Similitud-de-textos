from googlesearch import search
import requests
from bs4 import BeautifulSoup
import math
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.tokenize import RegexpTokenizer


def calcular_similitud_coseno(texto1, texto2):
    # Tokenizar los textos
    tokens_texto1 = word_tokenize(texto1)
    tokens_texto2 = word_tokenize(texto2)

    # Eliminar tokens de puntuación
    tokenizer = RegexpTokenizer(r'\w+')
    tokens_texto1 = tokenizer.tokenize(texto1)
    tokens_texto2 = tokenizer.tokenize(texto2)

    # Convertir los tokens a minúsculas
    tokens_texto1 = [token.lower() for token in tokens_texto1]
    tokens_texto2 = [token.lower() for token in tokens_texto2]

    # Eliminar tokens stopwords
    stopwords_es = set(stopwords.words('spanish'))
    tokens_texto1 = [token for token in tokens_texto1 if token.lower() not in stopwords_es]
    tokens_texto2 = [token for token in tokens_texto2 if token.lower() not in stopwords_es]
    
    #crear conjunto de palabras que hacen match
    tokens_match = set(tokens_texto1).intersection(set(tokens_texto2))
   
    # Crear conjunto de palabras únicas
    palabras_unicas = set(tokens_texto1 + tokens_texto2)
    
    # Calcular frecuencia de palabras en cada texto
    frecuencia_texto1 = {palabra: tokens_texto1.count(palabra) for palabra in palabras_unicas}
    frecuencia_texto2 = {palabra: tokens_texto2.count(palabra) for palabra in palabras_unicas}

    # Calcular los productos internos de los vectores
    producto_interno = sum(frecuencia_texto1[palabra] * frecuencia_texto2[palabra] for palabra in palabras_unicas)

    # Calcular las normas de los vectores
    norma_texto1 = math.sqrt(sum(frecuencia_texto1[palabra] ** 2 for palabra in palabras_unicas))
    norma_texto2 = math.sqrt(sum(frecuencia_texto2[palabra] ** 2 for palabra in palabras_unicas))

    # Calcular la similitud del coseno
    similitud_coseno = producto_interno / (norma_texto1 * norma_texto2)

    return round(similitud_coseno,2)


def buscar_en_web(query, umbral):
    resultados = search(query, lang='es', num=2, stop=4, pause=2)

    sitios_relevantes=[]
    for resultado in resultados:
        print (resultado)
        try:
            response = requests.get(resultado)
        except TypeError as e:
            return e
        
        if response.status_code == 200:
            html_content = response.text
            soup = BeautifulSoup(html_content, 'html.parser')
            text_content = ''
            for element in soup.find_all(['p']):
                text_content += element.get_text()
            
            if text_content!="":
                val=calcular_similitud_coseno(text_content,query)
                print(val)
                if val>=umbral:
                    sitios_relevantes.append(resultado)
            
    return sitios_relevantes

texto1="El principito narra la historia de un piloto que, mientras intenta reparar su avión averiado en medio del desierto del Sahara, se topa con un pequeño príncipe proveniente del asteroide B 612, que le pide insistentemente que le dibuje un cordero y que nunca olvida una pregunta. El piloto empezará a descubrir la fascinante historia del principito, que comienza en su asteroide, donde vivía con tres volcanes y se entretenía arrancando las malas hierbas y viendo puestas de sol. Un día, en el suelo del asteroide, nace una flor. El principito la cuida y atiende con dedicación, pero la flor es dramática y caprichosa, y esto le molesta. Entonces, decide abandonar su hogar y emprender un viaje por el universo en busca de un amigo. En la travesía, que llevará al principito a visitar varios asteroides hasta llegar a la Tierra, conocerá a un variado grupo de excéntricos personajes que lo convencen de lo extraño que es el mundo de los adultos, tan ocupados siempre en asuntos serios e importantes, que se olvidan de disfrutar la vida. En la Tierra, el principito entrará en contacto con animales, flores y personas. Será allí donde, antes de encontrar al piloto, conocerá al zorro, quien le revelará la importancia de la amistad y el valor del amor que siente hacia su flor. Será la nostalgia por ella y la decepción que le causa el mundo de los adultos lo que lo motivará a regresar a su planeta."
umbral=0.5
sitios=buscar_en_web(texto1, umbral)
print(sitios)

