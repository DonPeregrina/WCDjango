from django.urls import path

from . import views # Importar views.py

urlpatterns = [
    path('wordcloud', views.wordcloud, name='wordcloud'),
    path('generator',views.cloud_gen, name='cloud.gen'),
]