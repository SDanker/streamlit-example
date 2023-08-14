#importar librerias
import streamlit as st
import pickle
import pandas as pd
#import reclamos_model as model
import pickle
from transformers import pipeline

def model():
    sentiment_analyzer = pipeline('sentiment-analysis', model='nlptown/bert-base-multilingual-uncased-sentiment')




def main():
    #titulo
    st.title('Modelamiento categorización de reclamos')
    
    texto=st.text_input('reclamo','')
    #title = st.text_input('Movie title', 'Life of Brian')


    def resultado(texto):
        # Frase que deseas analizar
        #texto = "Me encanta esta película, es realmente emocionante y conmovedora."
        

        # Realiza el análisis de sentimiento
        resultados = model.sentiment_analyzer(texto)

        for resultado in resultados:
            label = resultado['label']
            score = resultado['score']
            
        return f'Sentimiento: {label}, Confianza: {score}'

    if st.button('RUN'):
       
        st.write(resultado(texto))
        

   

if __name__ == '__main__':
    main()
    