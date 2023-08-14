#importar las librerias necesarias
import pickle
from transformers import pipeline

# Carga el modelo preentrenado para análisis de sentimiento en español
sentiment_analyzer = pipeline('sentiment-analysis', model='nlptown/bert-base-multilingual-uncased-sentiment')




