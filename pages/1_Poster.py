import streamlit as st

st.title('Partick Litter Plan Poster 🌿')


st.image('images/Partick_Litter_Plan.jpg', width=400)

with open('images/Partick_Litter_Plan.pdf', "rb") as file:
    btn = st.download_button(
            label="Download Poster PDF",
            data=file,
            file_name="Partick_litter_Plsn.pdf",
            mime="image/pdf"
          )
    
    
st.image('images/by-nc.png', width=100)
"""
[CC BY-NC 4.0 DEED License](https://creativecommons.org/licenses/by-nc/4.0/)
"""

