import streamlit as st
from PIL import Image

st.title('顔認識アプリ')

uploaded_file = st.file_uploader("choose an image...", type='jpg')
if uploaded_file is not None:
    img = Image.open(uploaded_file)
    st.image(img, caption='uploaded Image.', use_column_width=True)
