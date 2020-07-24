# Import libraries
import pickle
import re

import nltk
import pandas as pd
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.preprocessing import LabelEncoder

# Import the dataset
path = r'C:\Users\ioann\Desktop\NLP Project\airline_sentiment.csv'
df_full = pd.read_csv(path, encoding='ISO-8859-1')

# Keep only columns of interest and rename them
df = df_full[['text', 'airline_sentiment']]
df.columns = ['tweet', 'sentiment']

# Encode the y variable
le = LabelEncoder()
df.sentiment = le.fit_transform(df.sentiment)

# Clean the text
nltk.download('stopwords')
corpus = []
for i in range(0, df.shape[0]):
    tweet = re.sub(r'@\w+', '', df['tweet'][i])
    tweet = re.sub('[^a-zA-Z]', ' ', df['tweet'][i])
    tweet = tweet.lower()
    tweet = tweet.split()
    ps = PorterStemmer()
    all_stopwords = stopwords.words('english')
    all_stopwords.remove('not')
    tweet = [ps.stem(word) for word in tweet if not word in set(all_stopwords)]
    tweet = ' '.join(tweet)
    corpus.append(tweet)

# Create the bag of words model
cv = CountVectorizer()
X = cv.fit_transform(corpus).toarray()
y = df.iloc[:, -1].values

# Split the dataset into the training and test set
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.20, random_state=0)

# Train the Naive Bayes model on the training set
classifier = MultinomialNB()
classifier.fit(X_train, y_train)

# Saving model to disk
pickle.dump(classifier, open('model.pkl', 'wb'))
pickle.dump(cv, open('cv.pkl', 'wb'))

# Make the predictions
y_pred = classifier.predict(X_test)
