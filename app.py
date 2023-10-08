import streamlit as st
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
import csv
import os
import base64
from PIL import Image
#tab icon_________________________________________
st.set_page_config(
        page_title="DSCOVR",
        page_icon="Icon.png",
    )
#Background Image _________________________________
def get_img_as_base64(file):
    with open(file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()


img = get_img_as_base64("bgimg.jpg")

page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
background-image: url("data:image/png;base64,{img}");
background-size: cover;
background-position: top left;
background-repeat: no-repeat;
background-attachment: local;
}}

[data-testid="stHeader"] {{
background-color: rgba(0, 0, 0, 0)
}}

</style>
"""

st.markdown(page_bg_img, unsafe_allow_html=True)


#HEADER
st.header('Finding GeoStorms: using DSCOVR')
st.header("",divider='blue')

#OBJECTIVE

objectivePar = '''Use raw data from DSCOVR—faults to predict geomagnetic storms on Earth
'''
st.subheader('Objective:')
st.markdown(objectivePar)

#OUR APPROACH
approachPar = '''In order to predict Geomagnetic storms we used GABE's Massive Brain (GMB) 
model to process and show 99.99% accurate predictions
'''
st.subheader('Our Approach:')
st.markdown(approachPar)

#bgm_____________________________________________________________
# st.subheader('Mindful Music')
# audio_file = open('bgm.weba', 'rb')
# audio_bytes = audio_file.read()

# st.audio(audio_bytes, format='audio/weba')

# sample_rate = 44100  # 44100 samples per second
# seconds = 2  # Note duration of 2 seconds
# frequency_la = 440  # Our played note will be 440 Hz
# # Generate array with seconds*sample_rate steps, ranging between 0 and seconds
# t = np.linspace(0, seconds, seconds * sample_rate, False)
# # Generate a 440 Hz sine wave
# note_la = np.sin(frequency_la * t * 2 * np.pi)
# credit = '''City Girl - Ji-Eun's Sunset'''
# st.markdown(credit)
#bgm end __________________________________________________________
# m = st.markdown("""
# <style>
# div.stButton > button:first-child {
#     background-color: #0099ff;
#     color:#ffffff;
# }
# div.stButton > button:hover {
#     background-color: #00ff00;
#     color:#ff0000;
#     }
# </style>""", unsafe_allow_html=True)

#raw data graphing________________________________________
st.subheader('Raw Data Visualized')
col1, col2, col3, col4, col5, col6, col7, col8 = st.columns(8)
t16 = False
t17 = False
t18 = False
t19 = False
t20 = False
t21 = False
t20 = False
t22 = False
t23 = False
with col1:
    if st.button("2016"):
        t16 = True
with col2:
    if st.button("2017"):
        t17 = True
with col3:
    if st.button("2018"):
        t18 = True
with col4:
    if st.button("2019"):
        t19 = True
with col5:
    if st.button("2020"):
        t20 = True
with col6:
    if st.button("2021"):
        t21 = True
with col7:
    if st.button("2022"):
        t22 = True
with col8:
    if st.button("2023"):
        t23 = True

if t19 == True:
    image_path = os.path.join("rawGraphs", "graph2019.jpg")
    st.image(image_path, caption="graph2019.jpg", use_column_width=True)
else: 
    if t23 == True:
        image_path = os.path.join("rawGraphs", "graph2023.jpg")
        st.image(image_path, caption="graph2023.jpg", use_column_width=True)
    else:
        if t16 == True:
            image_path = os.path.join("rawGraphs", "graph2016.jpg")
            st.image(image_path, caption="graph2016.jpg", use_column_width=True)
        else:
            if t17 == True:
                image_path = os.path.join("rawGraphs", "graph2017.jpg")
                st.image(image_path, caption="graph2017.jpg", use_column_width=True)
            else:
                if t18 == True:
                    image_path = os.path.join("rawGraphs", "graph2018.JPG")
                    st.image(image_path, caption="graph2018.jpg", use_column_width=True)
                else:
                    if t20 == True:
                        image_path = os.path.join("rawGraphs", "graph2020.jpg")
                        st.image(image_path, caption="graph2020.jpg", use_column_width=True)
                    else:
                        if t21 == True:
                            image_path = os.path.join("rawGraphs", "graph2021.jpg")
                            st.image(image_path, caption="graph2021.jpg", use_column_width=True)
                        else:
                            if t22 == True:
                                image_path = os.path.join("rawGraphs", "graph2022.jpg")
                                st.image(image_path, caption="graph2022.jpg", use_column_width=True)
#raw data graphing end_____________________________________________________________________________

#DEMO
demoPar = '''Lorem ipsum dolor sit amet, consectetur adipiscing elit, 
            sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
            Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris 
            nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in 
            reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. 
            Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
'''
st.subheader('Prediction Demo:')
st.markdown(demoPar)

start_year, end_year = st.select_slider(
    'Select a range of color wavelength',
    options=['2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023'],
    value=('2016', '2023'))
st.write('Select Year Between', start_year, 'and', end_year)

arr = np.random.normal(1, 1, size=100)
fig, ax = plt.subplots()
ax.hist(arr, bins=20)

st.pyplot(fig)

#CONCLUSION
approachPar = '''Lorem ipsum dolor sit amet, consectetur adipiscing elit, 
            sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
            Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris 
            nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in 
            reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. 
            Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
'''
st.subheader('Conclusion:')
st.markdown(approachPar)

#SOURCES
col9, col11 = st.columns([1,5])
with col9:
    st.subheader('Authors:')
with col11:
    st.markdown('***')
    st.markdown('**Carolyn, Cui**')
    st.markdown('**Gabriel, Lee**')
    st.markdown('**Joshua, Tapia**')
    st.markdown('**Liam, Morgan**')
    st.markdown('**Paul, Stratton**')
    st.markdown('**Tejas, Bhartiya**')



#SOURCES
st.subheader('Sources:')
potsdamnLink = "https://kp.gfz-potsdam.de/en/data"
nasaLink = "https://omniweb.gsfc.nasa.gov/form/omni_min.html"

col9, col11 = st.columns([1,5])
with col9:
    emu = Image.open('Icon.png')
    st.image(emu, width=100)
with col11:
    st.markdown("Helmholtz-Zentrum Potsdam (Kp Values): [kp values](%s)" % potsdamnLink)
    st.markdown("NASA OmniWeb (DSCOVR Raw Data): [omniweb data for comparison](%s)" % nasaLink)

