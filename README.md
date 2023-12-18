# Kaggle Competition: Truly Native?

This repository contains code for processing the data and building the model for [Truly Native?](https://www.kaggle.com/competitions/dato-native/data?select=5.zip "Link to Truly Native? Kaggle competition") Kaggle competition organized by Dato.

**_Main objective:_** predict whether the content in an HTML file was sponsored or not on [StumbleUpon](https://www.stumbleupon.com/).

## Project setup

Follow these steps to get the set up for the project ready and running on your local instance.

### Prerequisites

- Python 3.7+
- `pip install -r requirements.txt`
- Download `*.zip` files that contain raw HTMLs from [Kaggle](https://www.kaggle.com/competitions/dato-native/data) and place under `data` folder

#### Expected directory structure

    .
    ├── data                   # Data files
    │   ├── raw                # Raw zip files downloaded from Kaggle
    │   ├── csv                # Transformed csv files
    │   └── html_targets.csv   # Targets csv file downloaded from Kaggle
    ├── models                 # Models, EDA, hyper parameter tuning Jupyter notebooks
    │   ├── eda.ipynb          # Exploratory analysis on the processed dataset
    │   ├── hp_tuning.ipynb    # Hyper parameter tuning for selected models
    │   └── models_eval.ipynb  # Model evaluation with the best parameters
    ├── app.py                 # Streamlit app
    ├── process_raw_html.py    # Extract features from zip files
    └── ...

## Running the project

1. Run `python3 process_raw_html.py` to extract features from zip files
2. Run `hp_tuning.ipynb` for hyper parameter tuning with Randomized Search
3. Run `model_eval.ipynb` to evaluate and save final model to `pickle` file

## Presentation

![Slide 1](/assets/Slide1.png)
![Slide 2](/assets/Slide2.png)
![Slide 3](/assets/Slide3.png)
![Slide 4](/assets/Slide4.png)
![Slide 5](/assets/Slide5.png)
![Slide 6](/assets/Slide6.png)
![Slide 7](/assets/Slide7.png)
![Slide 8](/assets/Slide8.png)
![Slide 9](/assets/Slide9.png)
![Slide 10](/assets/Slide10.png)
![Slide 11](/assets/Slide11.png)
![Slide 12](/assets/Slide12.png)
![Slide 13](/assets/Slide13.png)
![Slide 14](/assets/Slide14.png)
![Slide 16](/assets/Slide16.png)
