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
    st.title("Colored Sketches")
    st.text("")
    st.text("") 
    st.sidebar.markdown('''
        Perceptual User Study form for Research Paper 
        ''')
    #st.sidebar.image(image_out("demo_data/LBL.png"))
    st.sidebar.markdown('''
    Thank you for visiting this page! Our team consisting of Ankita Ghosh, Manisimha Varma, Harsh Rathod, Sameer Saxena, V Manushree and Parna Chowdhury have worked on a research project on the problem statement of generating coloured sketches from photographic images.

We request you to view our results on this site and fill a survey form which will help us analyse the results produced by our team. We request you to help our research by following the given steps and thank you in advance for your time and response.
- A) Every time you click on the generate button, 10 random results are generated and displayed.
- B) View at least 50 results, that is, generate a minimum of 5 set of results. There is no limit to maximum, you can generate and view as many set of results as you wish. We request you to keep a count of the number of times you generate results as we will require it for our statistical analysis. 
- C) In the form, please fill your name, number of sets of results viewed and categorize yourself as either general user or a user with artistic background.
- D) Answer the questions 5,6,7 with respect to both the results: colored outline and colored sketch. You are required to answer the question in a score ranging from 1 to 5 according to the following legend:\nLink to the form: https://forms.office.com/r/CJjhvfmg6s\n
1: Very Poor\n
2: Bad\n
3: Average\n
4: Good\n
5: Perfect\n

Link to the form: https://forms.office.com/r/CJjhvfmg6s
For any queries, message Manushree (+918838451020).
    ''')
    
    st.sidebar.markdown('''''')

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
    page_title="Colored Sketches"
    )
    stream_run()