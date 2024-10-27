#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 23:33:56 2024

@author: estebanjimenez
"""

import streamlit as st
#from langchain.chat_models import ChatOpenAI
import os

# Leer la API Key de OpenAI desde las variables de entorno
#OPENAI_KEY = os.getenv('OPENAI_KEY')

# Función para análisis de código
#def analyze_code(code_snippet):
    #chat = ChatOpenAI(api_key=OPENAI_KEY, model_name="gpt-4")
    #response = chat.run([{"role": "user", "content": code_snippet}])
    #return response

# Mostrar la página de análisis de código
def show_code_analyzer_page ():
    st.title("Análisis de Código")
    st.tittle("En construccion")

    #code = st.text_area("Ingresa tu código:")
    #if st.button("Analizar"):
        #if code:
            #result = analyze_code(code)
            #st.write(result)
       # else:
            #st.error("Por favor ingresa un código.")

