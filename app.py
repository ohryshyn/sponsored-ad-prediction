import streamlit as st
import urllib.request
from process_raw_html import get_html_features

st.title('Discover if a website is sponsored or not')
html = st.text_input("Enter your website link here")
if st.button('Get Features'):
    with urllib.request.urlopen(html) as url:
        html = url.read().decode('utf-8')
    features = get_html_features(html)
    st.write(
        f"This is the title of your web page <span style='color:purple; font-weight:bold'>{features['title']}</span>", unsafe_allow_html=True)
    st.write(
        f"The number of scripts on your web page is **{features['num_scripts']}**")
