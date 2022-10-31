import os
import bs4 as bs
import pandas as pd

RAW_HTML_FOLDER_PATH = 'data/raw_html_files'

def get_title(soup):
    # get title of the html file
    return soup.title.string

def get_num_headers(soup):
    # get number of headers in the html file
    headers = soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])
    return len(headers)

def get_num_paragraphs(soup):
    # get number of paragraphs in the html file
    paragraphs = soup.find_all('p')
    return len(paragraphs)

def get_num_links(soup):
    # get number of links in the html file
    links = soup.find_all('a')
    return len(links)

def get_num_images(soup):
    # get number of images in the html file
    images = soup.find_all('img')
    return len(images)

def get_num_tables(soup):
    # get number of tables in the html file
    tables = soup.find_all('table')
    return len(tables)

def get_num_lists(soup):
    # get number of lists in the html file
    lists = soup.find_all(['ul', 'ol'])
    return len(lists)

def get_num_forms(soup):
    # get number of forms in the html file
    forms = soup.find_all('form')
    return len(forms)

def get_num_inputs(soup):
    # get number of inputs in the html file
    inputs = soup.find_all('input')
    return len(inputs)

def get_num_buttons(soup):
    # get number of buttons in the html file
    buttons = soup.find_all('button')
    return len(buttons)

def get_num_scripts(soup):
    # get number of scripts in the html file
    scripts = soup.find_all('script')
    return len(scripts)

def get_num_styles(soup):
    # get number of styles in the html file
    styles = soup.find_all('style')
    return len(styles)

def get_num_iframes(soup):
    # get number of iframes in the html file
    iframes = soup.find_all('iframe')
    return len(iframes)

def get_num_embeds(soup):
    # get number of embeds in the html file
    embeds = soup.find_all('embed')
    return len(embeds)

def get_num_of_lines(soup):
    # get number of lines in the html file
    return len(soup.text.splitlines())

def get_num_of_words(soup):
    # get number of words in the html file
    return len(soup.text.split())

def get_num_of_characters(soup):
    # get number of characters in the html file
    return len(soup.text)

def get_num_of_unique_words(soup):
    # get number of unique words in the html file
    return len(set(soup.text.split()))

def get_num_of_unique_characters(soup):
    # get number of unique characters in the html file
    return len(set(soup.text))

# loop through all the html files in the raw html folder
for file in os.listdir(RAW_HTML_FOLDER_PATH):
    with open(f"{RAW_HTML_FOLDER_PATH}/{file}", 'r') as f:
        soup = bs.BeautifulSoup(f, 'html.parser')
        # create a dictionary to store the features from each html file
        features = {
            'filename': file,
            'title': get_title(soup),
            'num_headers': get_num_headers(soup),
            'num_paragraphs': get_num_paragraphs(soup),
            'num_links': get_num_links(soup),
            'num_images': get_num_images(soup),
            'num_tables': get_num_tables(soup),
            'num_lists': get_num_lists(soup),
            'num_forms': get_num_forms(soup),
            'num_inputs': get_num_inputs(soup),
            'num_buttons': get_num_buttons(soup),
            'num_scripts': get_num_scripts(soup),
            'num_styles': get_num_styles(soup),
            'num_iframes': get_num_iframes(soup),
            'num_embeds': get_num_embeds(soup),
            'num_of_lines': get_num_of_lines(soup),
            'num_of_words': get_num_of_words(soup),
            'num_of_characters': get_num_of_characters(soup),
            'num_of_unique_words': get_num_of_unique_words(soup),
            'num_of_unique_characters': get_num_of_unique_characters(soup)
        }
        # write the features to a dataframe
        df = pd.DataFrame(features, index=[0])
        break
