from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

from predict import make_prediction


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = '0f1ee8b5e176fe7108309291fc363a04'

    class TweetForm(FlaskForm):
        tweet = StringField('tweet', validators=[DataRequired()])
        submit = SubmitField('Predict Sentiment')

    @app.route('/', methods=['GET', 'POST'])
    def home():
        form = TweetForm()
        if request.method == 'POST':
            return redirect(url_for('predict', tweet=request.form['tweet']))
        return render_template('home.html', form=form)

    @app.route('/predict')
    def predict():
        tweet = request.args.get('tweet', None)
        if tweet == None:
            return redirect(url_for('home'))
        prediction = make_prediction(tweet)
        return render_template('predict.html', prediction_text=prediction)

    return app
# if __name__ == "__main__":
#    app.run(host='0.0.0.0')
