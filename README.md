An end to end machine learning project.

We start by building an NLP model that predicts tweet sentiment.
Dataset found here: https://www.kaggle.com/crowdflower/twitter-airline-sentiment

We then create a Flask web app. 
It allows the user to input his/her tweet and get back the model's result.
The app is set up to be deployed on a production grade server with waitress.

Finally we Dockerize our application.