import bs4 as bs
import zipfile
from multiprocessing import Pool
import glob
import pandas as pd


def get_title(soup):
    # get title of the html file if it exists, if not, return none
    title = soup.title
    if title:
        # remove new line characters
        return title.text.replace('\n', '').strip()
    else:
        return None


def get_language(soup):
    # get language of the html file
    try:
        lang = soup.find('html').get('lang')
        if lang:
            return lang
        else:
            return None
    except:
        return None


def get_raw_text(soup):
    # get raw text from html body and remove new line characters if it exists
    raw_body = soup.body
    if raw_body:
        return raw_body.text.replace('\n', '').strip()
    else:
        return None


def get_num_headers(soup):
    # get number of headers in the html file
    headers = soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])
    return len(headers)


def get_num_paragraphs(soup):
    # get number of paragraphs in the html file
    paragraphs = soup.find_all('p')
    return len(paragraphs)


def get_num_tags(soup):
    # get number of tags in the html file
    return len(soup.find_all(True))


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


def get_num_italic_words(soup):
    # get all italic words in the html file
    italic_words = soup.find_all('i')
    return len(italic_words)


def get_num_bold_words(soup):
    # get all bold words in the html file
    bold_words = soup.find_all(['b', 'strong'])
    return len(bold_words)


def get_num_of_characters(soup):
    # get number of characters in the html file
    return len(soup.text)


def get_num_of_unique_words(soup):
    # get number of unique words in the html file
    return len(set(soup.text.split()))


def get_num_of_unique_characters(soup):
    # get number of unique characters in the html file
    return len(set(soup.text))


def get_num_of_digits(soup):
    # get number of digits in the html file
    return len([c for c in soup.text if c.isdigit()])


def get_html_features(html):
    # apply all parsing functions above to a given html file and returns a dictionary of features
    soup = bs.BeautifulSoup(html, 'html.parser')
    # create a dictionary of features
    html_features = {
        'filename': '',
        'title': get_title(soup),
        'language': get_language(soup),
        'raw_text': get_raw_text(soup),
        'num_headers': get_num_headers(soup),
        'num_paragraphs': get_num_paragraphs(soup),
        'num_tags': get_num_tags(soup),
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
        'num_lines': get_num_of_lines(soup),
        'num_words': get_num_of_words(soup),
        'num_italic_words': get_num_italic_words(soup),
        'num_bold_words': get_num_bold_words(soup),
        'num_characters': get_num_of_characters(soup),
        'num_unique_words': get_num_of_unique_words(soup),
        'num_unique_characters': get_num_of_unique_characters(soup),
        'num_digits': get_num_of_digits(soup)
    }
    return html_features


def process_zip(zip_file_path):
    html_features_list = []
    i = 1
    with zipfile.ZipFile(zip_file_path, 'r') as f:
        for html_file in f.namelist():
            if html_file.endswith('.txt'):
                raw_html = f.read(html_file)
                print(
                    f"Processing file {i} of {len(f.namelist())} in {zip_file_path}")
                html_features = get_html_features(raw_html)
                html_features['filename'] = html_file.split('/')[-1]
                html_features_list.append(html_features)
                i += 1
    df = pd.DataFrame(html_features_list)
    df.to_csv('data/csv/' + zip_file_path.split('/')
              [-1].split('.')[0] + '.csv', index=False)


if __name__ == '__main__':
    zip_files = glob.glob('data/raw/*.zip')
    with Pool(4) as p:
        p.map(process_zip, zip_files)
