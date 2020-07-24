import pickle
import re

import nltk
from flask import Flask, render_template, request, redirect
from flask_wtf import FlaskForm
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = '0f1ee8b5e176fe7108309291fc363a04'
model = pickle.load(open('model.pkl', 'rb'))
cv = pickle.load(open('cv.pkl', 'rb'))


class TweetForm(FlaskForm):
    tweet = StringField('tweet', validators=[DataRequired()])
    submit = SubmitField('Predict Sentiment')


@app.route('/', methods=['GET', 'POST'])
def home():
    form = TweetForm()
    if form.validate_on_submit():
        return redirect(url_for('predict'))
    return render_template('home.html', form=form)


def process_review(new_review):
    new_review = str(new_review)
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


@app.route('/predict')
def predict():
    processed_tweet = process_review(request.form.values())
    prediction = predict_sentiment(processed_tweet)
    return render_template('predict.html', prediction_text=f'The tweet has a {sentiment_dict[str(prediction)]} sentiment')


if __name__ == "__main__":
    app.run(debug=True)
