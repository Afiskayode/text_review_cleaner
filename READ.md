# Text Review Cleaner

This Python script automates the text preprocessing of customer reviews. It reads a CSV file, removes punctuation, converts text to lowercase, and filters out English stopwords using the Natural Language Toolkit (NLTK). 

## Prerequisites

You need Python 3 installed on your machine. You can download it from [python.org](https://python.org).

## Setup and Installation

1. Download or save the script as `main.py`.
2. Create a folder named `data` in the same directory as `main.py`.
3. Place your input CSV file inside that folder and name it exactly `TestReviews.csv`. 

> **Important:** Your `TestReviews.csv` file must have a column named `review`.

4. Open your terminal or command prompt and install the required libraries:
```bash
pip install pandas nltk
```

## How to Run

Run the script locally using the following command:
```bash
python main.py
```

## What the Script Does
* Downloads the NLTK `stopwords` dataset automatically on the first run.
* Cleans the text in the `review` column.
* Saves the output to `data/cleaned_reviews.csv`.
* Prints a 5-row preview of the cleaned data to your terminal.
