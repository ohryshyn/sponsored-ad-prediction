import streamlit as st
import s3fs
import random
import bs4 as bs
import urllib.request
import pickle
import pandas as pd
import randfacts
from process_raw_html import get_html_features

fs = s3fs.S3FileSystem(anon=False)


@st.experimental_singleton()
def read_file(filename):
    with fs.open(filename, 'rb') as f:
        return pickle.load(f)


MODEL = read_file('nativead-model/webapp_rf.pkl')
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
    st.title('Truly native? 👀')
    st.subheader(
        'Check if a website would be considered sponsored on StumbleUpon!')
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
                    msg = 'This website **would be sponsored** on **<span style="color:#f74425">StumbleUpon</span>**.'
                    st.markdown(msg, unsafe_allow_html=True)
                else:
                    msg = 'This website **would not be sponsored** on **<span style="color:#f74425">StumbleUpon</span>**.'
                    st.markdown(msg, unsafe_allow_html=True)
            with st.expander("See more"):
                st.write(
                    f"This is the title of your web page <span style='color:purple; font-weight:bold'>{features['title']}</span>", unsafe_allow_html=True)
                st.write(
                    f"The number of scripts on your web page is **{features['num_scripts']}**")
                st.markdown("""---""")
                st.write("_Did you know?_")
                st.write(f"{randfacts.get_fact()}")
            st.write(
                "GitHub repository for this project available **[at this link](https://github.com/oleh-ai/sponsored-ad-prediction/blob/main/app.py)**")

        except UnicodeDecodeError:
            st.error('Cannot decode this URL. Please try another link.')
        except ValueError as e:
            if len(e.args) > 0 and e.args[0] == "unknown url type: ''":
                st.error(
                    'Cannot process an empty string. Please enter a valid URL.')
            else:
                st.error('Something went wrong. Please try another link.')
                st.error(e)
        except:
            st.error('Cannot process this URL. Please try another link.')
            st.error(e)


if __name__ == '__main__':
    main()
