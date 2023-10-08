import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

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
