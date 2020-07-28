import pickle
import re

import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

nltk.download('stopwords')
model = pickle.load(open('model.pkl', 'rb'))
cv = pickle.load(open('cv.pkl', 'rb'))


def preprocess(new_review):
    new_review = re.sub(r'@\w+', '', new_review)
    new_review = re.sub('[^a-zA-Z]', ' ', new_review)
    new_review = new_review.lower()
    new_review = new_review.split()
    ps = PorterStemmer()
    all_stopwords = stopwords.words('english')
    all_stopwords.remove('not')
    new_review = [ps.stem(word)
                  for word in new_review if not word in set(all_stopwords)]
    new_review = ' '.join(new_review)
    new_corpus = [new_review]
    return new_corpus


def predict_sentiment(new_corpus):
    new_X_test = cv.transform(new_corpus).toarray()
    new_y_pred = model.predict(new_X_test)
    return new_y_pred


sentiment_dict = {
    '[0]': 'negative',
    '[1]': 'neutral',
    '[2]': 'positive'
}


def make_prediction(s):
    # print(str(s))
    s = preprocess(str(s))
    prediction = predict_sentiment(s)
    return f'The tweet has a {sentiment_dict[str(prediction)]} sentiment'
