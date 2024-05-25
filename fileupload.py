import streamlit as st
import pandas as pd
from PIL import Image

st.title('File Uploading')
st.subheader('1. Uploading an Image')
img_file = st.file_uploader('Upload your Image', type = ['png','jpeg'])
if img_file is not None:
     file_details = {'file_name': img_file.name, 'file_type': img_file.type,
     'file_size':img_file.size}
     st.write(file_details)
     st.image(Image.open(img_file))

st.subheader('1. Uploading csv')
csv_file = st.file_uploader('Upload your Image', type = ['csv','txt'])
if csv_file is not None:
     file_details = {'file_name': csv_file.name, 'file_type': csv_file.type,
     'file_size':csv_file.size}
     st.write(file_details)
     st.table(csv_file)
