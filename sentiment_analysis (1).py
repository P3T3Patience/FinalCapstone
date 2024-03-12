import spacy
import pandas as pd
from nltk.corpus import stopwords
from spacytextblob.spacytextblob import SpacyTextBlob

nlp = spacy.load('en_core_web_sm')
stop_words = set(stopwords.words('english'))
nlp.add_pipe("spacytextblob")

# Accessed data and cleaned, removed stop words, etc.
data = pd.read_csv(r'amazon_product_reviews.csv', encoding='utf8')
data['filtered_data'] = data['reviews.text'].apply(lambda x: ' '.join([word for word in x.split() if word not in (stop_words)]))
reviews_data = data['filtered_data']
reviews_data = reviews_data.dropna()
row_input = int()

# Input for which review to score - In loop to remove 'not integer' errors.
while row_input == int():
    row_input = input("Enter a review number (0 - 5000): ")
    if row_input.isdigit() == True:
        row_input = int(row_input)
        if row_input <5001:
            reviews_data = reviews_data.values[row_input]
            print(reviews_data)
            data_as_string = str(reviews_data)

            # Tokenisation
            doc = nlp(data_as_string)
            token_list = [token for token in doc]

            # Getting polarity score
            polarity = doc._.blob.polarity
            print(polarity)
        elif row_input.isdigit() == False:
            print("Error: Please provide an integer between 0-5000")
            row_input = int()
    elif row_input.isdigit() == False:
            print("Error: Please provide an integer between 0-5000")
            row_input = int()

