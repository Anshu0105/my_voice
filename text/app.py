import streamlit as st
st.header("Text To Speech App🎙️")
st.subheader("welcome to Anshuman's Project🤖")

st.divider()
from gtts import gTTS
import pygame

r=st.text_input("Kya sunoge bhai")
language = 'en'

myobj = gTTS(text=r, lang=language, slow=False)
myobj.save("welcome.mp3")

pygame.mixer.init()
pygame.mixer.music.load("welcome.mp3")
pygame.mixer.music.play()
st.audio("welcome.mp3")