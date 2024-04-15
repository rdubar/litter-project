import streamlit as st
from settings import poster_path

st.title('Poster 🌿')

st.image(f'{poster_path}.jpg', caption="Partick Litter Plan Poster", width=400)

with open(f'{poster_path}.pdf', "rb") as file:
    btn = st.download_button(
            label="Download Poster PDF",
            data=file,
            file_name="Partick_litter_Plsn.pdf",
            mime="image/pdf"
          )