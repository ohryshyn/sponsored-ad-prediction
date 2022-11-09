import streamlit as st
import random
import bs4 as bs
import urllib.request
import pickle
import pandas as pd
from process_raw_html import get_html_features


MODEL = pickle.load(open('rf_model.pkl', 'rb'))
EXCLUDE_COLS = ['filename', 'language', 'raw_text', 'title']


def get_html_from_url(url):
    with urllib.request.urlopen(url) as url:
        html = url.read().decode('utf-8')
    return html


def get_prediction_features(features):
    features = {k: features[k] for k in set(
        list(features.keys())) - set(EXCLUDE_COLS)}
    return features


def get_prediction_result(features):
    df = pd.DataFrame(features, index=[0])
    prediction = MODEL.predict(df)
    if prediction[0] == 1:
        return True
    else:
        return False


def get_random_image_link(html):
    soup = bs.BeautifulSoup(html, 'html.parser')
    images = soup.find_all('img')
    try:
        random_image = random.choice(images)
        return random_image['src']
    except:
        return None


def main():
    st.title('Truly native? 🤡')
    st.subheader('Check if a website was sponsored for a native ad or not')
    st.text('Enter the URL to see the prediction')
    url = st.text_input('URL')
    if st.button('Predict if native!'):
        try:
            with st.spinner('Fitting the model...'):
                html = get_html_from_url(url)
                features = get_html_features(html)
                pred_features = get_prediction_features(features)
                prediction = get_prediction_result(pred_features)
                if prediction:
                    st.write("This website was **sponsored** for a native ad.")
                else:
                    st.write(
                        "This website was **not sponsored** for a native ad.")
            with st.expander("See more"):
                st.write(
                    f"This is the title of your web page <span style='color:purple; font-weight:bold'>{features['title']}</span>", unsafe_allow_html=True)
                st.write(
                    f"The number of scripts on your web page is **{features['num_scripts']}**")
                try:
                    st.image(get_random_image_link(html))
                    st.caption('Random image from the web page')
                except AttributeError as e:
                    st.write('No images found on the web page')
                except:
                    pass
        except ValueError as e:
            if len(e.args) > 0 and e.args[0] == "unknown url type: ''":
                st.error(
                    'Cannot process an empty string. Please enter a valid URL.')
            else:
                st.error('Please enter a valid URL.')


if __name__ == '__main__':
    main()
