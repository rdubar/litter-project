import streamlit as st
from settings import poster_path

import os

# Check if the file exists
file_path = '/mount/src/litter-project/images/Partick_litter_Plan.jpg'
if os.path.exists(file_path):
    st.write('File exists')
else:
    st.write('File does not exist')
    # Optionally list files in the directory
    directory_path = '/mount/src/litter-project/images/'
    if os.path.exists(directory_path):
        files = os.listdir(directory_path)
        st.write('Files in directory:', files)
    else:
        st.write('Directory does not exist')

st.title('Poster 🌿')

st.write(f'{poster_path}.jpg')

st.image(f'{poster_path}.jpg', caption="Partick Litter Plan Poster", width=400)

with open(f'{poster_path}.pdf', "rb") as file:
    btn = st.download_button(
            label="Download Poster PDF",
            data=file,
            file_name="Partick_litter_Plsn.pdf",
            mime="image/pdf"
          )