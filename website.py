import streamlit as st
import requests
from PIL import Image

API_URL = "https://kyo-va-la-pj6drrveta-od.a.run.app"

quote = requests.get(API_URL,timeout=20).json()

st.title('Kyo va là !')

st.write(quote['Kyo'])

kyo = Image.open('kyo.jpg')
st.image(kyo)

st.write(
    'Please refresh to get another random Kyo quote to enlight your day !'
)
