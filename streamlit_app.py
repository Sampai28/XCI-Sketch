import streamlit as st
import os
from PIL import Image
import random 
import numpy as np
import pandas as pd

@st.cache(ttl=3600, max_entries=10)
def image_out(image):
    return Image.open(image)

def stream_run():
    file_name = list(pd.read_csv('cost.csv')['file_name'])
    randomlist = random.sample(range(1, 1001), 10)
    image = []
    for i in randomlist:
        image.append(os.path.join('demo_data/plt_inference', file_name[i]))
    st.title("XCI-Sketch: Extraction of Color Information from Images for Generation of Colored Outlines and Sketches")
    st.text("")
    st.text("") 
    #st.sidebar.image(image_out("demo_data/LBL.png"))
    

    #image = "demo_data/15_4.png"
    if st.button("Generate"):  
        randomlist = random.sample(range(1, 1001), 10)
        image = []
        for i in randomlist:
            image.append(os.path.join('demo_data/plt_inference', file_name[i]))
        
    st.image(np.array(image_out(image[0]))[150:350,:], use_column_width=True)  
    st.image(np.array(image_out(image[1]))[150:350,:], use_column_width=True)  
    st.image(np.array(image_out(image[2]))[150:350,:], use_column_width=True)  
    st.image(np.array(image_out(image[3]))[150:350,:], use_column_width=True)  
    st.image(np.array(image_out(image[4]))[150:350,:], use_column_width=True)  
    st.image(np.array(image_out(image[5]))[150:350,:], use_column_width=True)  
    st.image(np.array(image_out(image[6]))[150:350,:], use_column_width=True)  
    st.image(np.array(image_out(image[7]))[150:350,:], use_column_width=True)  
    st.image(np.array(image_out(image[8]))[150:350,:], use_column_width=True)  
    st.image(np.array(image_out(image[9]))[150:350,:], use_column_width=True)  

if __name__ == "__main__":
    st.set_page_config(
    initial_sidebar_state="expanded",
    page_title="XCI-Sketch: Extraction of Color Information from Images for Generation of Colored Outlines and Sketches"
    )
    stream_run()