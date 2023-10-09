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

objectivePar = '''Using raw, past to present data taken by DSCOVR, we want to make a model that can predict upcoming geomagnetic storms.
'''
st.subheader('Objective:')
st.markdown(objectivePar)

#Background

backPar = '''Geomagnetic storms can severely impact important systems like GPS and electrical power grids on Earth. The National Oceanic 
and Atmospheric Administration’s (NOAA’s) space weather station, the Deep Space Climate Observatory (DSCOVR), can measure the strength 
and speed of the solar wind in space, which enables us to predict geomagnetic storms, but the DSCOVR machine is past its optimal life 
expectancy and the collected data is prone to error.
'''
st.subheader('Background')
st.markdown(backPar)

#OUR APPROACH
approachPar = '''We used multiple different machine learning models from Single-step dense,
Multi-Step Dense and Single-Step LSTM that
gave us an average of 40% accuracy 
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

#Raw data processing info
st.subheader('Raw Data Process')
rawDat = '''The given data from DSCOVR provided three magnetic vectors 
(among 50 values of unlabeled raw data) which were the most consistent 
form of data given. Using the magnitude of these vectors alongside the 
Kp index values which represent strength of magnetic storms, we were able 
to visualize the data for the years and observe correlations within. The 
raw data is incredibly faulty, missing large swathes of dates, containing an 
abundance of NaN values, and even duplicating many values. However through 
processing, we were able to get the data to a workable point so that it could 
be used as a dataset for training and so that it could create these readable graphs. 
The scatter plot shows the simple trend of "As magnitude increases, Kp index also 
increases" which is relatively consistent. The heatmap is used to help represent the 
incomprehensible scale of these datasets, with each year's graph containing hundreds 
of thousands of datapoints.
'''
st.markdown(rawDat)

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
if t16 == False and t17 == False and t18 == False and t19 == False and t20 == False and t21 == False and t22 == False and t23 == False:#Jacob's ladder
    image_path = os.path.join("rawGraphs", "graph2016.jpg")
    st.image(image_path, caption="graph2016.jpg", use_column_width=True)
else:
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
demoPar = '''
'''
st.subheader('Prediction Demo:')
st.markdown(demoPar)
st.image('graph.png', caption="graph.png")
start_year, end_year = st.select_slider(
    'Select a year to see prediction',
    options=['2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023'],
    value=('2016', '2023'))
st.write('Select Year Between', start_year, 'and', end_year)

arr = np.random.normal(1, 1, size=100)
fig, ax = plt.subplots()
ax.hist(arr, bins=20)

st.pyplot(fig)

#CONCLUSION
approachPar = '''Due to time constraints we were not able to finish
everything that we wanted to do, however in the future we look forward,
to make the graph reactive with user input to show or accuracy and also
be able to make prediction on future dates
'''
st.subheader('Conclusion:')
st.markdown(approachPar)

#SOURCES
col9, col11, col12 = st.columns([1,2,4])
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
with col12:
    st.markdown('***')
    cC = "https://www.linkedin.com/in/carolyn-cui-60879919a/"
    gL = "https://www.linkedin.com/in/gabriel-lee-0676ba222/"
    jT = "https://www.linkedin.com/in/joshua-tapia-swe/"
    lM = "https://www.linkedin.com/in/liamamorgan27/"
    pS = "https://www.linkedin.com/in/paulstratton56/"
    tB = "https://www.linkedin.com/in/tejas-bhartiya/"
    st.markdown("[https://www.linkedin.com/in/carolyn-cui-60879919a/](%s)" % cC)
    st.markdown("[https://www.linkedin.com/in/gabriel-lee-0676ba222/](%s)" % gL)
    st.markdown("[https://www.linkedin.com/in/joshua-tapia-swe/](%s)" % jT)
    st.markdown("[https://www.linkedin.com/in/liamamorgan27/](%s)" % lM)
    st.markdown("[https://www.linkedin.com/in/paulstratton56/](%s)" % pS)
    st.markdown("[https://www.linkedin.com/in/tejas-bhartiya/](%s)" % tB)

    




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

