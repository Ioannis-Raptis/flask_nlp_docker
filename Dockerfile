FROM python:3.8.2
WORKDIR /app
COPY ./requirements.txt /app

RUN pip install -r requirements.txt
COPY . /app

CMD ["waitress-serve", "--call", "flaskr:create_app"]