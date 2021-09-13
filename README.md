An NLP model served through a simple Flask web page, that tells you whether the tweet provided has positive or negative emotion. 

We start by building an NLP model that predicts tweet sentiment.
Dataset found here: https://www.kaggle.com/crowdflower/twitter-airline-sentiment

We then create a Flask web app. 
It allows the user to input his/her tweet and get back the model's result.
The app is set up to be deployed on a production grade server with waitress.

Finally we Dockerize our application.

To run the app, first download the image:
docker pull  ioannisid/flask_nlp
Then run it with:
docker run -p 8080:8080 ioannisid/flask_nlp
Go to http://localhost:8080/ in your browser.
There you have it :)
