import streamlit as st

st.title('Poster 🌿')

st.image('images/Partick_litter_Plan.jpg', caption="Partick Litter Plan Poster", width=400)

with open("images/Partick_litter_Plan.pdf", "rb") as file:
    btn = st.download_button(
            label="Download Poster PDF",
            data=file,
            file_name="Partick_litter_Plsn.pdf",
            mime="image/pdf"
          )