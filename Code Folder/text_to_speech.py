import nltk
import streamlit as st
from textblob import TextBlob
from streamlit_option_menu import *
from streamlit_extras.keyboard_url import keyboard_to_url
from streamlit_lottie import st_lottie
from streamlit_extras.colored_header import colored_header
import json as js
import time
import googletrans
from googletrans import Translator
from googletrans import LANGUAGES
import gtts
from gtts import gTTS
import os
import requests
import pandas as pd
#__________________________________________________________


class language_ai :

    def process(self):
        st.set_page_config(page_title='Speech Synthesis Project By Praveen', layout="wide")


        with st.sidebar:  # Navbar
            ss = option_menu(
                menu_title="Speech Synthesis",
                options=['Intro','Process'],
                icons=['mic-fill', ''],
                menu_icon='alexa',
                default_index=0,
            )

        def lottie(filepath):
            with open(filepath, 'r') as file:
                return js.load(file)


        st.markdown("<style>div.block-container{padding-top:1rem;}</style>", unsafe_allow_html=True)

        col1, col2, col3 = st.columns([4, 7, 3])

        col2.markdown(
            "<h1 style='font-size: 100px;'><span style='color: cyan;'>Speech</span> <span style='color: white;'>Synthesis</span> </h1>",
            unsafe_allow_html=True)
        col1, col2, col3 = st.columns([4, 7, 3.7])
        with col2:
            colored_header(
                label="",
                description="",
                color_name="blue-green-70", )
        col2.write("")
        col2.write("")
        col2.write("")
        col2.write("")

        col4,col1, col2, col3 = st.columns([3,10, 3, 10])
        with col1:
            file = lottie("text.json")
            st_lottie(
                file,
                speed=1,
                reverse=False,
                loop=True,
                quality='low',
                # renderer='svg',
                height=400,
                width=500,
                key=None
            )
        with col3:
            file = lottie("speech.json")
            st_lottie(
                file,
                speed=1,
                reverse=False,
                loop=True,
                quality='low',
                # renderer='svg',
                height=400,
                width=500,
                key=None
            )

        col1,col2,col3 = st.columns([4,7,4.3])
        col2.markdown(
            "<h1 style='font-size: 40px;'><span style='color: cyan;'>Provide</span> <span style='color: white;'>Text</span> </h1>",
            unsafe_allow_html=True)

        input = col2.text_input("")
        with col2:
            if st.button('Proceed'):
                # English Language Specified Here
                language = 'en'

                # Object Creation for gTTS Class
                text_to_speech = gTTS(text=input, lang=language, slow=False)

                # Save Audio File
                text_to_speech.save("output.mp3")

                os.system("start output.mp3")
#___________________________________________________________________________________________________________________________________________





# Object Creation

object = language_ai()
object.process()