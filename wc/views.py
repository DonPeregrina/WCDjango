#Esta es la aplicación

from django.shortcuts import render
#Visualisación
import numpy as np
import pandas as pd
from os import path
import Image

#Generador de wordcloud
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
from .models import ArticleData, Category, Keyword

#Nos ayuda a mostrar la imagen en html
import matplotlib.pyplot as plt
import io
import urllib, base64

#Le decimos que abrá el archivo
df = pd.read_csv("pokemon_data.csv", index_col=0)

df.head()

df.columns = ['Name', 'Type1', 'Type2', 'HP', 'Attack', 'Defense', 'SpAtk','SpDef', 'Speed', 'Generation', 'Legendary']

df[["Name", "Type1","HP"]].head()

def wordcloud (text):
    # Checa nuestro documento
    text = df.description[0]

    # Crea y genera una imagen wordcloud
    wordcloud = WordCloud(max_font_size=50, max_words=100, background_color="white").generate(text)

    # La despliega
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    image = io.BytesIO()
    plt.savefig(image, format='png')
    image.seek(0)  # rewind the data
    string = base64.b64encode(image.read())

    image_64 = 'data:image/png;base64,' + urllib.parse.quote(string)
    return image_64

def cloud_gen(request):
    text = ''
    for i in ArticleData.objects.all():
        if __name__ == '__main__':
            text += i.text
    wordcloud = word_cloud(text)
    return render(request, 'articles/index.html', {'wordcloud':wordcloud})